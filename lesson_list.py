# list
import copy

l = [1, 2, 2, 4, 5, 5, 55]
print(l[0])
print(l[-1])
print(l[-2])
print(l[3:])
print(len(l))

print(list('abcdefg'))

n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(n)
print(n[::2])
print(n[::-1])

a = list('abc')
x = list('1234')
print([a, x])

z = [a, x]

print(z[0][1])

s = list('abcdefg')

print(s)
s[0] = 'X'
print(s)
s[2:5] = list('ABC')
print(s)

s.append(100)
print(s)
s.insert(0, 23)
print(s)
s.pop()
print(s)
s.pop(0)
print(s)
del s[0]
print(s)
s.remove('b')
print(s)

a = list('12345')
b = list('67890')
x = a + b
print(a + b)
a += b
print(a)

r = [1, 2, 3, 4, 3, 4, 3, 5]
print(r.index(3))
print(r.index(3, 3))
print(r.count(3))

if 5 in r:
    print('exsist')

r.sort()
print(r)
r.sort(reverse=True)
print(r)
r.reverse()
print(r)

# 文字列をリストに分割する
s = 'My name is Mike'
to_split = s.split(' ')
print(to_split)

# リストを結合させる
x = ' '.join(to_split)
print(x)

# ヘルプを表示する
# print(help(list))

i = [1, 2, 3, 4, 5]
j = i
print('i =', i)
print('j =', j)
j[0] = 100
# jを変更しただけだが、iの値も変更される
print('i =', i)
print('j =', j)

x = [1, 2, 3, 4, 5]
y = x.copy()
y[0] = 100
# copyを使用すれば元の変数に影響はでない
print('x =', x)
print('y =', y)

