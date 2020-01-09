# 01. 「パタトクカシーー」
# 「パタトクカシーー」という文字列の1,3,5,7文字目を取り出して連結した文字列を得よ．

def odd_extract(word: str) :
    return word[0:7:2]

odd_extract('パタトクカシーー')