# decorator

def print_info(func):
    """
    decorator
    :param func:
    :return:
    """
    def wrapper(*args, **kwargs):
        print('start')
        result = func(*args, **kwargs)
        print('end')
        return result
    return wrapper

def print_more(func):
    """
    decorator
    :param func:
    :return:
    """
    def wrapper(*args, **kwargs):
        print('func', func.__name__)
        print('args:', args)
        print('kwards', kwargs)
        result = func(*args, **kwargs)
        print('result', result)
        return result
    return wrapper

def add_num(a, b):
    return a + b

# print('start')
# r = add_num(29 + 29)
# print('end')
#
# print(r)

f = print_info(add_num)
r = f(10, 20)
print(r)

# 上側のデコレーターから呼び出される
@print_info
@print_more
def add_num2(a, b):
    return a + b

r2 = add_num2(10, 20)
print(r2)