# 25. テンプレートの抽出
# 記事中に含まれる「基礎情報」テンプレートのフィールド名と値を抽出し，辞書オブジェクトとして格納せよ．

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
    temp_dict[key] = value

pprint.pprint(temp_dict)

