# 09. Typoglycemia
# スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，
# それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ．
# ただし，長さが４以下の単語は並び替えないこととする．
# 適当な英語の文（例えば"I couldn't believe that I could actually understand
#  what I was reading : the phenomenal power of the human mind ."）を与え，
# その実行結果を確認せよ．

import random

def typoglycemia(sentence: str) :
    word_list = sentence.split()

    for i in range(len(word_list)) :
        checked_word = word_list[i]
        if len(checked_word) > 4 :
            first_char = checked_word[0]
            last_char = checked_word[-1]
            exchanged_char = ''.join(random.sample(checked_word[1:-1:1], len(checked_word) - 2))
            word_list[i] = first_char + exchanged_char + last_char

    return ' '.join(word_list)

typoglycemia("I couldn't believe that I could actually understand \
what I was reading : the phenomenal power of the human mind .")