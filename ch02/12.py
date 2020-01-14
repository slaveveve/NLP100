# 12. 1列目をcol1.txtに，2列目をcol2.txtに保存
# 各行の1列目だけを抜き出したものをcol1.txtに，
# 2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．確認にはcutコマンドを用いよ．

def extract_col(relative_path: str,  new_file_nm, row: int) :
    with open(relative_path, 'r', encoding='utf8') as data:
        row_data = ''
        for line in data.readlines() :
            delimitered_line = line.split('\t')
            row_data += (delimitered_line[row - 1] + '\n')

        with open(new_file_nm, 'w', encoding='utf8') as new_file :
            new_file.write(row_data)

extract_col('hightemp.txt', 'col1.txt', 1)
extract_col('hightemp.txt', 'col2.txt', 2)

# ※確認時unixコマンド
# $ cut -f 1 hightemp.txt 
# > 高知県
# > 埼玉県
# > 岐阜県
# > 山形県
# > 山梨県
# > 和歌山県
# > 静岡県
# > 山梨県
# > 埼玉県
# > 群馬県
# > 群馬県
# > 愛知県
# > 千葉県
# > 静岡県
# > 愛媛県
# > 山形県
# > 岐阜県
# > 群馬県
# > 千葉県
# > 埼玉県
# > 大阪府
# > 山梨県
# > 山形県
# > 愛知県

# $ cut -f 2 hightemp.txt 
# > 江川崎
# > 熊谷
# > 多治見
# > 山形
# > 甲府
# > かつらぎ
# > 天竜
# > 勝沼
# > 越谷
# > 館林
# > 上里見
# > 愛西
# > 牛久
# > 佐久間
# > 宇和島
# > 酒田
# > 美濃
# > 前橋
# > 茂原
# > 鳩山
# > 豊中
# > 大月
# > 鶴岡
# > 名古屋
