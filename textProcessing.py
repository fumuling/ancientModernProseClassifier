import createVocab
import sklearn

def createVec(train_words_set):
    if train_words_set:
        # train_data_list, test_data_list, train_class_list, test_class_list = sklearn.cross_validation.train_test_split(
        #     data_list, class_list, test_size=test_size)
        print("载入成功")
        words_list = list(train_words_set)
        words_dict = {}
        for word in words_list:
            if words_dict.has_key(word):
                words_dict[word] += 1
            else:
                words_dict[word] = 1

        words_tuple_list = sorted(words_dict.items(), key= lambda x:x[1], reverse=True)







    else:
        raise Exception("载入失败")


if __name__ == "__main__":
    createVec()