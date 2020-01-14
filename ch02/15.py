# 15. 末尾のN行を出力
# 自然数Nをコマンドライン引数などの手段で受け取り，入力のうち末尾のN行だけを表示せよ．
# 確認にはtailコマンドを用いよ．

def get_tail_rows(file, n: int) :
    ext_rows = [s.replace('\n', '') for s in file.readlines()[-n:]]
    for row in ext_rows :
        print(row)

with open('hightemp.txt', 'r', encoding='utf8') as f :
    input_num = int(input('取得行数入力'))
    get_tail_rows(f, input_num)

# ※確認時unixコマンド(5行表示を想定)
# $ tail -5 hightemp.txt 
# > 埼玉県	鳩山	39.9	1997-07-05
# > 大阪府	豊中	39.9	1994-08-08
# > 山梨県	大月	39.9	1990-07-19
# > 山形県	鶴岡	39.9	1978-08-03
# > 愛知県	名古屋	39.9	1942-08-02