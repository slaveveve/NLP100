# 36. 単語の出現頻度
# 文章中に出現する単語とその出現頻度を求め，出現頻度の高い順に並べよ．

import pprint

sentences = __import__('30').parsed_sentence()
frequency = {}

for i in sentences :
    for j in i :
        key = j['surface'] + r'\t' + j['pos'] + r'\t' + j['pos1']
        if key not in frequency :
            frequency[key] = 1
        else :
            frequency[key] += 1

pprint.pprint(sorted(frequency.items(), key=lambda x:x[1], reverse=True))