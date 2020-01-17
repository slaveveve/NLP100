# 24. ファイル参照の抽出
# 記事から参照されているメディアファイルをすべて抜き出せ．

import gzip
import json
import re
def extract_england() :
    with gzip.open('jawiki-country.json.gz', 'r') as f :
        for line in f :
            article = json.loads(line)
            if article['title'] == 'イギリス' :
                return article['text']

article = extract_england()
#"(\|.*?)の部分は、前半の\がなければファイル名の先頭1文字しか取得してこない"
for line in re.findall(r'\[\[(ファイル|File):([^|]+?)(\|.*?)+\]\]', article) :
        print(line[1])
