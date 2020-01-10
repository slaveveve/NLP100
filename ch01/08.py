# 08. 暗号文
# 与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．

# 英小文字ならば(219 - 文字コード)の文字に置換
# その他の文字はそのまま出力
# この関数を用い，英語のメッセージを暗号化・復号化せよ．

def cipher(words: str) :
    return_words = ''
    for i in range(len(words)) :
        if words[i].islower() :
            return_words += chr(219 - ord(words[i]))
        else :
            return_words += words[i]
    
    return return_words

original_words = '9mm Parabellum Bullet'
encryption_words = cipher(original_words)

print(f'暗号化前:{original_words}')
print(f'暗号化:{encryption_words}')
print(f'復号化:{cipher(encryption_words)}')