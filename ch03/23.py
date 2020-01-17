# 23. セクション構造
# 記事中に含まれるセクション名とそのレベル（例えば"== セクション名 =="なら1）を表示せよ．

import gzip
import json

def extract_england() :
    with gzip.open('jawiki-country.json.gz', 'r') as f :
        for line in f :
            article = json.loads(line)
            if article['title'] == 'イギリス' :
                return article['text']

article = extract_england()
splitted_article = article.split('\n')
for line in splitted_article :
    if '==' in line :
        replaced_line = line.replace(' ', '')
        print(f'{replaced_line.replace("=", "")}:{int(replaced_line.count("=") / 2) - 1}')

