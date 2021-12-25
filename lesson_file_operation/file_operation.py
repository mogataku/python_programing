# ファイル操作

import os
import pathlib
import glob
import shutil

# ファイルの存在確認
print(os.path.exists('test.csv'))
# ファイルであるかどうか
print(os.path.isfile('test.csv'))
# ディレクトリの存在確認
print(os.path.isdir('lesson_file_operation'))
# ファイル名の変更
# os.rename('text.txt', 'rename.txt')
# ファイルの内容が等しいファイルを作成
# os.symlink('rename.txt', 'symLink.txt')
# ディレクトリを作成
# os.mkdir('test_dir')
# ディレクトリを削除
# os.rmdir('test_dir')

# pathlib.Path('empty.txt').touch()
# os.remove('empty.txt')

# os.mkdir('test_dir')
# os.mkdir(('test_dir/test_dir2'))
# ディレクトリ内にあるディレクトリを表示
# print(os.listdir('test_dir'))
# 作成したディレクトリ内にファイルを作成
# pathlib.Path('test_dir/test_dir2/empty.txt').touch()
# shutil.copy('test_dir/test_dir2/empty.txt',
#             'test_dir/test_dir2/empty2.txt')
# print(glob.glob('test_dir/test_dir2/*'))

# shutil.rmtree('test_dir')

print(os.getcwd())