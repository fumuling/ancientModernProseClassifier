from langconv import *

def Traditional2Simplified(sentence):
    '''
    将sentence中的繁体字转为简体字
    :param sentence: 待转换的句子
    :return: 将句子中繁体字转换为简体字之后的句子
    '''
    sentence = Converter('zh-hans').convert(sentence)
    return sentence

if __name__=="__main__":


    # 读取文件
    fn=open('D:\周景怡\周景怡\WHU\大三上\文本理解与数据挖掘\文言文数据qingxi.txt','r+',encoding="utf-8") # 打开文件
    s=fn.readlines()
    fn.close
    for line in s:
        line = line.strip('\n')
        simplified_sentence = Traditional2Simplified(line)
        #print(simplified_sentence)

        f=open("D:\周景怡\周景怡\WHU\大三上\文本理解与数据挖掘\文言文简体.txt", "a",encoding="utf-8")
        f.writelines(simplified_sentence)
        f.writelines("\r\n")
        f.close()

