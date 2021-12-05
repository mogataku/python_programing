# 標準ライブラリ

s = 'awhifhwhfhifhiaowhfihawhfhiofhew'

d = {}
for c in s:
    if c not in d:
        d[c] = 0
    d[c] += 1
print(d)

d2 = {}
for c in s:
    d2.setdefault(c, 0)
    d2[c] += 1
print(d2)

# 標準ライブラリを読み込む際は、importが必要になる
from collections import defaultdict
d3 = defaultdict(int)
for c in s:
    d3[c] += 1
print(d3)