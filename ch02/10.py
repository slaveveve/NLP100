# 10. 行数のカウント
# 行数をカウントせよ．確認にはwcコマンドを用いよ．

def line_count(relative_path: str) :
    file = open(relative_path, 'r', encoding='utf8')
    return len(file.readlines())

line_count('hightemp.txt')

# ※確認時unixコマンド
# $ wc -l hightemp.txt
# > 24 hightemp.txta