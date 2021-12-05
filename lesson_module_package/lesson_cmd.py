# コマンドライン引数

# terminal

# ls フォルダの一覧を表示する

# python lesson_cmd.phy 指定したフォルダを実行する

import sys

# コマンドラインで引数を設定する
# python lesson_cmd.phy arg1 arg2
print(sys.argv)

for i in sys.argv:
    print(i)