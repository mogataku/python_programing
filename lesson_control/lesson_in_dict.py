# in_dict

w = ['mon', 'tue', 'wed']
f = ['coffee', 'milk', 'water']

d = {}
for x,y in zip(w, f):
    d[x] = y

print(d)

d = {x: y for x, y in zip(w, f)}
print(d)

# 集合内包表記
s = set()

for i in range(10):
    s.add(i)

print(s)

s = {i for i in range(10) if i % 2 == 0}
print(s)

# ジェネレーター内包表記
def g():
    for i in range(10):
        yield i

g = g()
print(type(g))
g = tuple(i for i in range(10))
print(g)
