# プロパティーを使った属性の設定

class Car(object):
    def __init__(self, model=None):
        self.model = model
    def run(self):
        print('run')

class ToyotaCar(Car):
    def run(self):
        print('fast')

class TeslaCar(Car):
    def __init__(self, model='Model S',
                 enable_auto_run=False,
                 password = '123'):
        super().__init__(model)
        # _がないため、自由に変更して良い
        # self.enable_auto_run = enable_auto_run
        # _があるため、propertyなどで変更方法を指定する
        self._enable_auto_run = enable_auto_run
        # __であるため、基本変更は行わない
        # self.__enable_auto_run = enable_auto_run

    @property
    def enable_auto_run(self):
        return self._enable_auto_run
    @enable_auto_run.setter
    def enable_auto_run(self, is_enable):
        if self.password == '456':
            self._enable_auto_run = is_enable
        else:
            raise ValueError
    def run(self):
        print('super fast')
    def auto_run(self):
        print('auto run')

tesla_car = TeslaCar('Model S', password='456')
print(tesla_car._enable_auto_run)

class T(object):
    pass

# 便利な方法ではあるが、エラーの原因になりやすい
t = T()
t.name = 'Mike'
t.age = 20
print(t.name, t.age)