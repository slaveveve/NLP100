# 06. 集合
# "paraparaparadise"と"paragraph"に含まれる文字bi-gramの集合を，
# それぞれ, XとYとして求め，XとYの和集合，積集合，差集合を求めよ．
# さらに，'se'というbi-gramがXおよびYに含まれるかどうかを調べよ．

def generate_bi_gram(sentence: str) :
    return set((sentence[i:i+2] for i in range(len(sentence) - 1)))

def contain_word(word_list: list, word: str) :
    if word in word_list :
        print(f'{word_list}に"{word}"は含まれています')
    else :
        print(f'{word_list}に"{word}"は含まれていません')


X = generate_bi_gram('paraparaparadise')
Y = generate_bi_gram('paragraph')

print(f'和集合:{X.union(Y)}')
print(f'積集合:{X.intersection(Y)}')
print(f'差集合:{X.difference(Y)}')

contain_word(X, 'se')
contain_word(Y, 'se')