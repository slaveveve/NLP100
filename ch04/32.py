# 32. 動詞の原形
# 動詞の原形をすべて抽出せよ．

sentences = __import__('30').parsed_sentence()

for i in sentences :
    for j in i :
        if j['pos'] == '動詞' :
            print(j['base'])