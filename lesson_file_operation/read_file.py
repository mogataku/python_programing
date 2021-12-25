# ファイルの読み込み

s = """\
AAA
BBB
CCC
DDD
"""

# with open('test3.text', 'w') as f:
#     f.write(s)

with open('test3.text', 'r') as f:
    # print(f.read())
    # while True:
    #     # 何文字づつ読み込むか
    #     chunk = 2
    #     line = f.read(chunk)
    #     print(line)
    #     if not line:
    #         break
    print(f.tell())
    print(f.read(1))
    # 何文字目を読み込むか
    f.seek(5)
    print(f.read(1))
    f.seek(15)
    print(f.read(1))
