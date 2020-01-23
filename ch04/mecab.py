import MeCab

# mecab = MeCab.Tagger('/usr/local/lib/mecab/dic/mecab-ipadic-neologd')
# print(mecab.parse('私の名前は太郎です'))

with open('neko.txt', 'r', encoding='utf8') as neko:
    mecab = MeCab.Tagger('/usr/local/lib/mecab/dic/mecab-ipadic-neologd')
    with open('neko.txt.mecab', 'w', encoding='utf8') as parsed_neko:
        parsed_neko.write(mecab.parse(neko.read()))