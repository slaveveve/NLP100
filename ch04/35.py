# 35. 名詞の連接
# 名詞の連接（連続して出現する名詞）を最長一致で抽出せよ．

import re

sentences = __import__('30').parsed_sentence()

articulation = ''
join_cnt = 0

for i in sentences :
    for j in range(len(i)) :
            
        # TODO 
        # print(j)

        if re.match('名詞', i[j]['pos']) and re.match(r'[^」「]', i[j]['surface']) \
            and re.match(r'[^—]', i[j]['surface']):
            
            # TODO 
            # print(f'surface:{i[j]["surface"]}')

            articulation += i[j]["surface"]
            join_cnt += 1
        elif join_cnt == 1 :
            articulation = ''
            join_cnt = 0
        elif join_cnt >= 2 :
            print(articulation)
            articulation = ''
            join_cnt = 0
