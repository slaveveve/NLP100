# 03. 円周率
# "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
# という文を単語に分解し，各単語の（アルファベットの）文字数を先頭から出現順に並べたリストを作成せよ．

import re

def count_word_len(sentence: str) :
    dropped_sentence = re.sub(r'[.,]', '', sentence)
    splitted_sentence =  dropped_sentence.split()
    count_word_len = ''.join(str(len(word)) for word in splitted_sentence)
    return count_word_len

count_word_len('Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.')