# importの相対パスと絶対パス

from lesson_package.lesson_talk import talk
from lesson_package.lesson_talk import animals
# from lesson_package.lesson_talk import *

print(animals.sing())
print(animals.cry())
print(talk.sing())
print(talk.cry())

try:
    from lesson_package import utils
except ImportError:
    from lesson_package.lesson_tools import utils

utils.say_twice('hello')