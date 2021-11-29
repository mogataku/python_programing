# generator
l = ['Good morning', 'Good afternoon', 'Good night']

for i in l:
    print(i)

def greeting():
    yield 'Good morning'
    yield 'Good afternoon'
    yield 'Good night'

# キューと同様の処理が行える
g = greeting()
print(next(g))
print('Mike')
print(next(g))
print('Sam')
print(next(g))
print('Sin')