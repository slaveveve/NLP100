# 26. 強調マークアップの除去
# 25の処理時に，テンプレートの値からMediaWikiの
# 強調マークアップ（弱い強調，強調，強い強調のすべて） を除去してテキストに変換せよ（参考: マークアップ早見表）．

import gzip
import json
import re
import pprint

def extract_england() :
    with gzip.open('jawiki-country.json.gz', 'r') as f :
        for line in f :
            article = json.loads(line)
            if article['title'] == 'イギリス' :
                return article['text']

def extract_temp(article : str) :
    start_temp = re.search(r'{{基礎情報 国\n', article).end()
    end_temp = re.search(r'(.*)\n}}\n',article).end()
    return article[start_temp:end_temp - 4]

article = extract_england()
org_temp = extract_temp(article)
find_temp = re.split(r'\n\|', org_temp)
temp_dict = {}

for temp in find_temp :
    key = temp.split(' = ')[0].strip('|')
    value = temp.split(' = ')[1]
    #25.pyにここを足しただけ
    value_splited_emphasized = re.sub(r'(\'{2}|\'{3}|\'{5})', '',value)
    temp_dict[key] = value_splited_emphasized

pprint.pprint(temp_dict)