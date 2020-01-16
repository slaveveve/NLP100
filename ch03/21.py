# 21. カテゴリ名を含む行を抽出
# 記事中でカテゴリ名を宣言している行を抽出せよ．

import gzip
import json

def extract_england() :
    with gzip.open('jawiki-country.json.gz', 'r') as f:
        for line in f :
            article = json.loads(line)
            if article.get('title') == 'イギリス' :
                return article['text']

article = extract_england()
splitted_article = article.split('\n')
for i in splitted_article :
    if 'Category' in i :
        print(i)