# scope name
animal = 'cat'

def f():
    print(animal)
    # ローカル変数を呼び出す前に、同名のグローバル変数は呼び出せない
    # animal = 'dog'
    print('local:', locals())

# fucからグローバル変数は読み込める
f()
print('global:', globals())