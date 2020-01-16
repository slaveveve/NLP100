# 20. JSONデータの読み込み
# Wikipedia記事のJSONファイルを読み込み，「イギリス」に関する記事本文を表示せよ．
# 問題21-29では，ここで抽出した記事本文に対して実行せよ．

import gzip
import json

def extract_england() :
    with gzip.open('jawiki-country.json.gz', 'r') as f:
        for line in f :
            article = json.loads(line)
            if article.get('title') == 'イギリス' :
                return article['text']

chk_article = extract_england()
print(chk_article)