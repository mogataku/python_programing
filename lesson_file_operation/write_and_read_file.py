# 書き込み読み込みモード

s = """\
AAA
BBB
CCC
DDD
"""

# w+ では新しいファイルを作成し、書き込み読み込みを実行する
with open('test4.text', 'w+') as f:
    f.write(s)
    f.seek(0)
    print(f.read())

# r+ では読み込むファイルが存在しないとエラーが発生する
with open('test4.text', 'r+') as f2:
    f2.write(s)
    f2.seek(0)
    print(f2.read())
