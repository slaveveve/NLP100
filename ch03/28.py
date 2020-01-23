# 28. MediaWikiマークアップの除去
# 27の処理に加えて，テンプレートの値からMediaWikiマークアップを可能な限り除去し，国の基本情報を整形せよ．

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
    value_splited_emphasized = re.sub(r'(\'{2}|\'{3}|\'{5})', '',value)
    value_splited_innner_link = value_splited_emphasized
    value_splited_innner_link = re.sub(r'\[\[([^|\]]+\|)*(.*?)\]\]', '\\2', value_splited_emphasized)

    value_splited_markdown = value_splited_innner_link
    # value_splited_markdown = re.sub(r'(<.*?/>)(</.*?>)(\{\{.*?\}\})', '', value_splited_innner_link)

    # 改行変換
    value_splited_markdown = re.sub(r'<br\s*?/>', '\n', value_splited_markdown)
    # <ref>タグ除去
    value_splited_markdown = re.sub(r'(?s)<ref[^>]*?/>|<ref[^>]*?>.*?</ref>', '', value_splited_markdown)
    # {{lang}}タグ変換
    value_splited_markdown = re.sub(r'{{lang\|.*?\|(.*?)}}', '\\1', value_splited_markdown)

    temp_dict[key] = value_splited_markdown

pprint.pprint(temp_dict)


