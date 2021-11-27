# none
is_empty = None
print(is_empty)

# is はオブジェクトを比較する
if is_empty is None:
    print('None 何も入っていないよ！！')

# true false
if(not 0):
    print('false')
if(1):
    print('true')
d = [1, 2, 3]
if(d):
    print('true')
d = []
if(not d):
    print('false')