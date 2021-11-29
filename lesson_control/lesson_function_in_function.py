# function in function
def outer(a, b):

    # 特定の関数内でのみ呼ばれる場合、関数内に入れた方が良い
    def plus(c, d):
        return c + d

    r = plus(a, b)
    print(r)

outer(1, 2)