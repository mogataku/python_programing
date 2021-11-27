# operator
a = 1
b = 1

# operatorのサンプルの一覧
print(a == b)
print(a != b)
print(a < b)
print(a > b)
print(a <= b)
print(a >= b)
print(a > 0 and b > 0)
print(a > 0 or b > 0)


# in not 使い方
y = [1, 2, 3]
x = 1

if x in y:
    print('in')

if x not in y:
    print('not in')

#  よくない例
c = 1
d = 2

if not c == d:
    print('not equal')
# if c != d: の方が良い

# よく使用する例
is_ok = True

if not is_ok:
    print('hello')
# if is_ok == True: より短い