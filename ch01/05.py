# 05. n-gram
# 与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．この関数を用い，
# "I am an NLPer"という文から単語bi-gram，文字bi-gramを得よ．

#※n-gram...
#任意の文字列や文書を連続したn個の文字で分割するテキスト分割方法．
# 特に，nが1の場合をユニグラム（uni-gram），2の場合をバイグラム（bi-gram），
# 3の場合をトライグラム（tri-gram）と呼ぶ．

def n_gram(n: int, sentence: str) :
    word_n_gram = []
    letter_n_gram = []
    word_list = sentence.split()

    word_n_gram = (word_list[i:i + n] for i in range(len(word_list) - n + 1))
    letter_n_gram = (sentence[i:i + n] for i in range(len(sentence) - n + 1))

    return list(word_n_gram), list(letter_n_gram)

n_gram(2, 'I am an NLPer')
