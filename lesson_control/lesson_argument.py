# argument
def menu(entry, drink, desert):
    print(entry)
    print(drink)
    print(desert)

menu(entry='beef', drink='coffee', desert='ice')

def menu2(entry='rice', drink='water', desert='none'):
    print(entry)
    print(drink)
    print(desert)

menu2(entry='beef', desert='ice')


# リストは初期化されないため、デフォルト引数に入れない方が良い
def test_func(x, l=[]):
    l.append(x)
    return l

y = [1, 2, 3]
r = test_func(100, y)
print(r)

print(test_func(1000))
print(test_func(1010))


# 位置関数のタプル化
def say_anything(word, *args):
    print(word)
    for arg in args:
        print(arg)

t = ('aba', 'cde')
say_anything('any', *t)
say_anything('hi', 'nice', 'to', 'me', 'too')