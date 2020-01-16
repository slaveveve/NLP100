# 17. １列目の文字列の異なり
# 1列目の文字列の種類（異なる文字列の集合）を求めよ．
# 確認にはsort, uniqコマンドを用いよ．

def unique_string_col_1(relative_path: str) :
    with open(relative_path, 'r', encoding='utf8') as f:
        col1_list = []
        for line in f.readlines() :
            delimitered_line = line.split('\t')
            col1_list.append(delimitered_line[0])

        return list(set(col1_list))

unique_string_col_1('hightemp.txt')


# ※確認時unixコマンド
# $ cat hightemp.txt | cut -f 1 | sort -u 
# > 千葉県
# > 埼玉県
# > 大阪府
# > 山形県
# > 山梨県
# > 岐阜県
# > 愛媛県
# > 愛知県
# > 群馬県
# > 静岡県
# > 高知県
# > 和歌山県