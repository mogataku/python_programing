# クラス変数

class Person(object):

    # selfを使用せずに変数を設定できる
    kind = 'human'

    def __init__(self, name):
        # self.kind = 'human'
        self.name = name
    def who_are_you(self):
        print(self.name, self.kind)

a = Person('A')
a.who_are_you()
b = Person('B')
b.who_are_you()

class T(object):

    # 他のインスタンスオブジェクトと共有される
    words = []

    def add_words(self, word):
        self.words.append((word))

c = T()
c.add_words('add1')
c.add_words('add2')
print(c.words)
d = T()
d.add_words('add3')
d.add_words('add4')
print(c.words)
print(d.words)