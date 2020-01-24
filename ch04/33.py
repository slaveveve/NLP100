# 33. サ変名詞
# サ変接続の名詞をすべて抽出せよ．

import re

sentences = __import__('30').parsed_sentence()

for i in sentences :
    for j in i :
        if j['pos1'] == 'サ変接続' and j['pos'] == '名詞' and re.match(r'[^*]', j['base']):
            print(j['base'])