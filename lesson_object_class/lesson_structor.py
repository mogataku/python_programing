# コンストラクタ　デストラクタ

class Person(object):
    def __init__(self, name):
        # コンストラクタ　一番初めに呼ばれる箇所
        self.name = name
        print(self.name)
    def say_something(self):
        print('I am {},Hello'.format(self.name))
        self.run()
    def run(self):
        print('running')
    def __del__(self):
        # デストラクタ　オブジェクトが使われなくなったときに呼ばれる箇所
        print('good bye')

person = Person('Mike')
person.say_something()

del person

print('$$$$$$$$$$$$')