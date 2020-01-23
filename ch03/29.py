# 29. 国旗画像のURLを取得する
# テンプレートの内容を利用し，国旗画像のURLを取得せよ．
# （ヒント: MediaWiki APIのimageinfoを呼び出して，ファイル参照をURLに変換すればよい）

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

#########################################################################################################


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
    value_splited_markdown = re.sub(r'<br\s*?/>', '\n', value_splited_markdown)
    value_splited_markdown = re.sub(r'(?s)<ref[^>]*?/>|<ref[^>]*?>.*?</ref>', '', value_splited_markdown)
    value_splited_markdown = re.sub(r'{{lang\|.*?\|(.*?)}}', '\\1', value_splited_markdown)

    temp_dict[key] = value_splited_markdown

# pprint.pprint(temp_dict['国旗画像'])

# 以下画像URL取得処理
import requests
import urllib

r = requests.get('https://ja.wikipedia.org/w/api.php?',
params = {
    'action': 'query',
    'format': 'json',
    'prop': 'imageinfo',
    'titles': 'File:' + re.sub(r'\s', '_',temp_dict['国旗画像']),
    'iiprop': 'url'
})

pprint.pprint(list(r.json()['query']['pages'].values())[0]['imageinfo'][0]['url'])