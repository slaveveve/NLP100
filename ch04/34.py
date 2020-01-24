# 34. 「AのB」
# 2つの名詞が「の」で連結されている名詞句を抽出せよ．

import re

sentences = __import__('30').parsed_sentence()

for i in sentences :
    for j in range(len(i)) :
        if re.match('の', i[j]['surface']) and re.match('助詞', i[j]['pos']) \
            and re.match('名詞', i[j - 1]['pos']) and re.match('名詞', i[j + 1]['pos']):
            print(f'{i[j - 1]["surface"]}の{i[j + 1]["surface"]}')