import tkinter
import tkinter.messagebox
import joblib
import sys
import jieba
from sklearn.feature_extraction.text import TfidfVectorizer
LABEL_MAP = ['现代文', '文言文', '诗', '词']

window = tkinter.Tk()
window.title("文本分类器")
window.geometry("600x400")
l1 = tkinter.Label(window, text = "请输入要分类的文本:")
l1.pack()
e = tkinter.Entry(window, show = None)
e.pack()

with open('characters-master/stop_words.txt', encoding='utf-8') as f:
    stop_words = [line.strip() for line in f.readlines()]
clf1 = joblib.load("MultinomialNB_clf_model.pkl")
clf2 = joblib.load("BernoulliNB_clf_model.pkl")
train_tfidf_vector = joblib.load("TF-IDF_model.pkl")


def MultinomialNB():
    var = e.get()
    word_list = jieba.lcut(var)
    documents = []
    words = [wl for wl in word_list if wl not in stop_words]
    sentence = ' '.join(words)
    documents.append(sentence)
    test_tfidf_vector = TfidfVectorizer(max_df=0.5, vocabulary=train_tfidf_vector.vocabulary_)
    test_x = test_tfidf_vector.fit_transform(documents)
    res = clf1.predict(test_x)
    ans = LABEL_MAP[res[0]]
    tkinter.messagebox.showinfo('提示', ans)


def BernoulliNB():
    var = e.get()
    word_list = jieba.lcut(var)
    documents = []
    words = [wl for wl in word_list if wl not in stop_words]

    sentence = ' '.join(words)
    documents.append(sentence)
    test_tfidf_vector = TfidfVectorizer(max_df=0.5, vocabulary=train_tfidf_vector.vocabulary_)
    test_x = test_tfidf_vector.fit_transform(documents)
    res = clf2.predict(test_x)
    ans = LABEL_MAP[res[0]]
    tkinter.messagebox.showinfo('提示', ans)

def on_closing():
    if tkinter.messagebox.askokcancel("Quit","现在就退出么"):
        window.destroy()

btn1 = tkinter.Button(window, text="用多项式朴素贝叶斯分类", command = MultinomialNB)
btn2 = tkinter.Button(window, text="用伯努利朴素贝叶斯分类", command = BernoulliNB)



btn1.pack()
btn2.pack()



window.protocol("WM_DELETE_WINDOW", on_closing)


window.mainloop()

sys.exit()