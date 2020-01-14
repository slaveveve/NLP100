# 16. ファイルをN分割する
# 自然数Nをコマンドライン引数などの手段で受け取り，入力のファイルを行単位でN分割せよ．
# 同様の処理をsplitコマンドで実現せよ．

import numpy as np

def split_rows(file, n: int) :
    rows = file.readlines()
    split_num = int(np.ceil(len(rows) / n))

    for i in range(split_num) :
        with open(f'16_splited_hightemp_by_code_{i}', 'w', encoding='utf8') as f :
            f.write(''.join(rows[i * split_num:(i + 1) * split_num]))

with open('hightemp.txt', 'r', encoding='utf8') as f :
    input_num = int(input('取得行数入力'))
    split_rows(f, input_num)

# ※確認時unixコマンド(5分割を想定)
# $ split -l 5 hightemp.txt 16_splited_hightemp_by_cui_
# > 以下ファイルが出力される
# > 16_splited_hightemp_by_cui_aa
# > 16_splited_hightemp_by_cui_ab
# > 16_splited_hightemp_by_cui_ac
# > 16_splited_hightemp_by_cui_ad
# > 16_splited_hightemp_by_cui_ae
