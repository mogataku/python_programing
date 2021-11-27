# enumerate
for i, fruit in enumerate(['apple', 'banana', 'orange']):
    print(i, fruit)


# zip
days = ['Mon', 'Tue', 'Wed']
fruits = ['apple', 'banana', 'orange']
drinks = ['coffee', 'tea', 'beer']

for day, fruit, drink in zip(days, fruits, drinks):
    print(day, fruit, drink)


# dictionary in for
d = {'x': 100, 'y': 200}

for k, v in d.items():
    print(k, ':', v)