# in list

t = {1, 2, 3, 4, 5}
t2 = {5, 6, 7, 8, 9, 10}

r = []
for i in t:
    r.append(i)

print(r)

s = [i for i in t if i % 2 == 0]
print(s)

# こちらの方がコードは読みやすい
r2 = []
for i in t:
    for j in t2:
        r2.append(i * j)
print(r2)

s2 = [i * j for i in t for j in t2]
print(s2)