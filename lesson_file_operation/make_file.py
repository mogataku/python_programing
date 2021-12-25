# ファイルの作成

# w ファイルを再作成
# a ファイルに追加
# r ファイルの読み込み
f = open('text.txt', 'w')
f.write('test')
print('I', 'can', 'print', sep='#', end='!', file=f)
f.close()

with open('text2.txt', 'w') as f2:
    f2.write('Test')