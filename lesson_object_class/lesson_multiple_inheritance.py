# 多重継承

class Person(object):
    def talk(self):
        print('talking')

class Car(object):
    def run(self):
        print('running')
    def talk(self):
        print('Do not talk')

# 左側に入れたクラスが優先されて呼び出される
class PersonCurRobot(Person, Car):
    def fly(self):
        print('fly')

person_car_robot = PersonCurRobot()
person_car_robot.run()
person_car_robot.fly()
person_car_robot.talk()