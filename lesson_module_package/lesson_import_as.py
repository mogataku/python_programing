# import as
import lesson_package.lesson_tools.utils
r = lesson_package.lesson_tools.utils.say_twice('hello')
print(r)

from lesson_package.lesson_tools import utils

# from を使うとパッケージ名を省略して記載ができる
r = utils.say_twice('good bye')
print(r)

r = utils.say_twice('say good bye')
print(r)

from lesson_package.lesson_tools.utils import say_twice as Utils
r = Utils('say good bye2')
print(r)