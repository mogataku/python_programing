# subprocessとコマンド

import subprocess

# ターミナルを実行できる
# subprocess.run(['ls'])
# 推奨されていない　シェルを実行できる checkでエラーコードを出力する
# r = subprocess.run('ls -al', shell=True, check=True)

p1 = subprocess.Popen(['ls', '-al'], stdut=subprocess.PIPE)
p2 = subprocess.Popen(
    ['grep', 'test'], stdin=p1.stdout, stdout=subprocess.PIPE
)
p1.stdout.close()
output = p2.communicate()[0]
print(output)
