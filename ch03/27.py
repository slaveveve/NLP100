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
    value_splited_emphasized = re.sub(r'(\'{2}|\'{3}|\'{5})', '',value)

    value_splited_innner_link = value_splited_emphasized

    # 一行に複数変換対象が存在する場合、以下のコメントアウトしてるコードだと、リンク以外も除去してしまう
    # if re.search(r'(\[\[.*\]\])(?!.*ファイル)', value_splited_emphasized) :
    #     print('この下need') 
    #     # 表示名の変換必要
    #     if re.search(r'\[\[.*?\|.*?\]\]', value_splited_emphasized) :
    #         #(?<=~): ~の後読み（~より後ろの文字列）
    #         #(?=~): ~の先読み（~より先の文字列）
    #         replace_value = re.search(r'(?<=\|).*(?=\]\])', value_splited_emphasized).group()
    #         print(replace_value)
    #         value_splited_innner_link = replace_value
    #     # 表示名の変換不要
    #     else :
    #         value_splited_innner_link = re.sub(r'(\[\[|\]\])', r'', value_splited_emphasized)
    # print(value_splited_emphasized)

    # 自力で解決できず。以下を参考に記述
    # (https://qiita.com/moriwo/items/badc6432cb925676089a#27-%E5%86%85%E9%83%A8%E3%83%AA%E3%83%B3%E3%82%AF%E3%81%AE%E9%99%A4%E5%8E%BB)

    value_splited_innner_link = re.sub(r'\[\[([^|\]]+\|)*(.*?)\]\]', '\\2', value_splited_emphasized)

    temp_dict[key] = value_splited_innner_link

pprint.pprint(temp_dict)

