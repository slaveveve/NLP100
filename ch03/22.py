# 22. カテゴリ名の抽出
# 記事のカテゴリ名を（行単位ではなく名前で）抽出せよ．

import gzip
import json
import re

def extract_england() :
    with gzip.open('jawiki-country.json.gz', 'r') as f:
        for line in f :
            article = json.loads(line)
            if article['title'] == 'イギリス' :
                return article['text']

article = extract_england()

splitted_article = article.split('\n')
for line in splitted_article :
    if 'Category' in line :
        print(re.split('[:|"\]"]', line)[1])