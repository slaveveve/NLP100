# 14. 先頭からN行を出力
# 自然数Nをコマンドライン引数などの手段で受け取り，入力のうち先頭のN行だけを表示せよ．
# 確認にはheadコマンドを用いよ．

def get_head_rows(file, n: int) :
    ext_rows = [s.replace('\n', '') for s in file.readlines()[:n]]
    for row in ext_rows :
        print(row)

with open('hightemp.txt', 'r', encoding='utf8') as f :
    input_num = int(input('取得行数入力'))
    get_head_rows(f, input_num)

# ※確認時unixコマンド(5行表示を想定)
# $ head -5 hightemp.txt 
# > 高知県	江川崎	41	2013-08-12
# > 埼玉県	熊谷	40.9	2007-08-16
# > 岐阜県	多治見	40.9	2007-08-16
# > 山形県	山形	40.8	1933-07-25
# > 山梨県	甲府	40.7	2013-08-10
