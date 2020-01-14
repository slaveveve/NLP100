# 13. col1.txtとcol2.txtをマージ
# 12で作ったcol1.txtとcol2.txtを結合し，元のファイルの1列目と2列目をタブ区切りで並べた
# テキストファイルを作成せよ．確認にはpasteコマンドを用いよ．

def read_file(relative_path: str) :
    with open(relative_path, 'r', encoding='utf8') as file:
        return [s.replace('\n', '') for s in file.readlines()]


def concat_2_files(file_1: list, file_2: list, new_file_nm: str) :
    concated_file = ''
    left_row = [s + ('\t') for s in file_1]
    right_row = [s + ('\n') for s in file_2]

    for i in range(len(file_1)) :
        concated_file += left_row[i]
        concated_file += right_row[i]
    
    with open(new_file_nm, 'w', encoding='utf8') as f :
        f.write(concated_file)


col_1 = read_file('col1.txt')
col_2 = read_file('col2.txt')

col_1

concat_2_files(col_1, col_2, 'concated_file.txt')

# ※確認時unixコマンド
# $ paste col1.txt col2.txt 
# > 高知県	江川崎
# > 埼玉県	熊谷
# > 岐阜県	多治見
# > 山形県	山形
# > 山梨県	甲府
# > 和歌山県	かつらぎ
# > 静岡県	天竜
# > 山梨県	勝沼
# > 埼玉県	越谷
# > 群馬県	館林
# > 群馬県	上里見
# > 愛知県	愛西
# > 千葉県	牛久
# > 静岡県	佐久間
# > 愛媛県	宇和島
# > 山形県	酒田
# > 岐阜県	美濃
# > 群馬県	前橋
# > 千葉県	茂原
# > 埼玉県	鳩山
# > 大阪府	豊中
# > 山梨県	大月
# > 山形県	鶴岡
# > 愛知県	名古屋
