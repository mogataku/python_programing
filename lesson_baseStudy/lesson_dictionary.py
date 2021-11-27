# dictionary
d = {'x': 10, 'y': 20}
print(type(d))
print(d['y'])
d['x'] = 1000
print(d)
d['y'] = 'jwjwjfiwejf'
print(d)
d['z'] = 123
print(d)
d[1] = 'joij'
print(d)

# dictionaryの他の書き方
print(dict(a=10, b=20))
print(dict([('a', 23), ('b', 43)]))

# dictionaryのメソッド
z = {'x': 10, 'y': 20}
print(z.keys())
print(z.values())
z2 = {'x': 1000, 'z': 80}
z.update(z2)
print(z)
print(z.get('x'))
print(z.get('fjioewj'))

# dictionaryのcopy
x = {'a': 1}
y = x
y['a'] = 1000
print(x)
print(y)

x2 = {'a': 1}
y2 = x2.copy()
y2['a'] = 1000
print(x2)
print(y2)

# dictionaryの使い道
fruits = {
    'apple': 100,
    'banana': 200,
    'orange': 50,
}
print(fruits['apple'])