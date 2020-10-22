import numpy
from collections import defaultdict



def cut(sentence):
    return sentence.split()

def create_vocab(path):
    words_set = set()
    with open(path, 'r',encoding='UTF-8') as f:
        for line in f.readlines():
            print(line)
            sentence = line.strip()
            if len(sentence) > 0 and not sentence.isdigit():
                for word in sentence.split():
                    if not word.isdigit():
                        words_set.add(word)
    return words_set


if __name__ == "__main__":
    path = "清洗后期刊论文.txt"
    print(create_vocab(path))