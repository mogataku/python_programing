# 絶対パス　こちらの方が使用されれている
# from lesson_package.lesson_tools import utils
# 相対パス
from ..lesson_tools import utils

def sing():
    return 'sing'

def cry():
    return utils.say_twice('cry')