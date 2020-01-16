# 19. 各行の1コラム目の文字列の出現頻度を求め，出現頻度の高い順に並べる
# 各行の1列目の文字列の出現頻度を求め，その高い順に並べて表示せよ．
# 確認にはcut, uniq, sortコマンドを用いよ．

from itertools import groupby

def count_and_sort_appearances(relative_path: str) :
    with open(relative_path, 'r', encoding='utf8') as f:
        col1_list = [s.split('\t')[0] for s in f.readlines()]
        col1_list.sort()
        grouped_col1_list = [(len(list(j)), i) for i, j in groupby(col1_list)]
        grouped_col1_list.sort(key=lambda line: float(line[0]), reverse=True)
        return grouped_col1_list

        

count_and_sort_appearances('hightemp.txt')

# ※確認時unixコマンド
# $ cat hightemp.txt | cut -f 1 | sort | uniq -c | sort -r
#>    3 群馬県
#>    3 山梨県
#>    3 埼玉県
#>    3 山形県
#>    2 静岡県
#>    2 愛知県
#>    2 岐阜県
#>    2 千葉県
#>    1 和歌山県
#>    1 高知県
#>    1 愛媛県
#>    1 大阪府