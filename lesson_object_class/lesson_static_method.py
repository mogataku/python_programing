# スタティックメソッドとクラスメソッド

class Person(object):

    kind = 'human'

    def __init__(self):
        self.x = 100

    @classmethod
    def what_is_your_kind(cls):
        return cls.kind

    @staticmethod
    def about(year):
        print('about time {}'.format(year))

a = Person()
print(a.x)
print(a.kind)
print(a.what_is_your_kind())

print('$$$$$$$$$$$$$$$$')

b = Person
# オブジェクトを作成しなくても、kindは確認できる
print(b.kind)
# クラスメソッドも確認できる
print(b.what_is_your_kind())

print('$$$$$$$$$$$$$$$$')

print(Person.what_is_your_kind())

Person.about(2021)