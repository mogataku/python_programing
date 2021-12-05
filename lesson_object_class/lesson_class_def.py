# クラス定義
s = 'jawjf;jf'
print(s.capitalize())

# objectの記載は描いた方が、継承で使いやすい
class Person(object):
    def say_something(self):
        print('Hello')

person = Person()
person.say_something()

def person(name):
    if name == 'a':
        print('hello')