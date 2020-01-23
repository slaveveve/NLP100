# 形態素解析結果（neko.txt.mecab）を読み込むプログラムを実装せよ．
# ただし，各形態素は表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）をキーとするマッピング型に格納し，
# 1文を形態素（マッピング型）のリストとして表現せよ．第4章の残りの問題では，ここで作ったプログラムを活用せよ．

import re
import pprint

# かなりの部分を以下を参考にしている…
# https://qiita.com/moriwo/items/1344ff9a0079d68a8cc4#30-%E5%BD%A2%E6%85%8B%E7%B4%A0%E8%A7%A3%E6%9E%90%E7%B5%90%E6%9E%9C%E3%81%AE%E8%AA%AD%E3%81%BF%E8%BE%BC%E3%81%BF
def parsed_sentence() -> [[{}]]:
    sentence = []
    with open('neko.txt.mecab', 'r', encoding='utf8') as f :
        for line in f.readlines() :
            if 'EOS' in line:
                yield sentence
                sentence = []
            else :
                sentence.append(generate_parsed_list(line))

def generate_parsed_list(line: str) :
    parsed_sentence = re.sub(r'\t', ',', line).split(',')
    return {
        'surface': parsed_sentence[0],
        'base': parsed_sentence[7],
        'pos': parsed_sentence[1],
        'pos1': parsed_sentence[2]
        }