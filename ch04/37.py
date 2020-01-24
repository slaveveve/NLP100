# 37. 頻度上位10語
# 出現頻度が高い10語とその出現頻度をグラフ（例えば棒グラフなど）で表示せよ．

import matplotlib as plt
frequency = __import__('36').frequency

frequency = sorted(frequency.items(), key=lambda x:x[1], reverse=True)
frequency[:10]

plt.pyplot()