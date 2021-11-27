# function definition
def say_something():
    print('hi')
# 関数は定義してから呼び出す
say_something()

def return_something():
    s = 'why'
    return s
result = return_something()
print(result)

def what_is_this(color):
    if color == 'red':
        return 'tomato'
    elif color == 'yellow':
        return 'banana'
    else:
        return 'I do not know'
print(what_is_this('white'))


def add_num(a: int, b: int) -> int:
    return  a + b
print(add_num(3, 4))