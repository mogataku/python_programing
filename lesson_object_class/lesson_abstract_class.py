# 抽象クラス
import abc
# 実行時、エラーが発生します

class Person(metaclass=abc.ABCMeta):
    def __init__(self, age = 1):
        self.age = age

    # 必ず実装してほしいクラスを記載する
    @abc.abstractmethod
    def drive(self):
        pass

class NoAdult(Person):
    def __init__(self, age = 1):
        if age < 18:
            super().__init__(age)
        else:
            raise ValueError
    def drive(self):
        raise Exception('No drive in Japan')

class Adult(Person):
    def __init__(self, age = 18):
        if age >= 18:
            super().__init__(age)
        else:
            raise ValueError

baby = NoAdult()
baby.drive()
adult = Adult()
