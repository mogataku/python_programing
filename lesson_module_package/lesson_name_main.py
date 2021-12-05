# _name_ _main_
print(__name__)
# このファイルから呼び出しているので、__main__が表示される

import lesson_package.lesson_talk.animals
# 他のファイル殻読み出した場合は、ファイル名が表示される

def main():
    lesson_package.lesson_talk.animals.sing()

print(main())