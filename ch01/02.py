## 

# 02. 「パトカー」＋「タクシー」＝「パタトクカシーー」
# 「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ．

def words_concat(word_1: str, word_2: str) :
    concated_word = ''.join(word_1[i] + word_2[i] for i in range(len(word_1)))
    return concated_word

words_concat('パトカー', 'タクシー')