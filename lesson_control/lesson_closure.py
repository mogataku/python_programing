# clusure
def outer(a, b):

    def inner():
        return a + b

    return inner
# innerが呼ばれるのみ
print(outer(2, 3))

f = outer(2, 3)
# inner()が呼び出される
r = f()
print(r)

# 同じ関数に引数を入れた状態で、保持したい際などに使用