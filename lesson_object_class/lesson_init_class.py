# クラスの初期化と変数

class Person(object):
    def __init__(self, name):
        self.name = name
        print(self.name)
    def say_something(self):
        print('I am {},Hello'.format(self.name))
        self.run()
    def run(self):
        print('running')

person = Person('Mike')
person.say_something()