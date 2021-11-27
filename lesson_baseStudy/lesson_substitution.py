# substitution
print('a is {}'.format('test'))

print('a is {} {} {}'.format(1, 2, 3))
print('a is {0} {1} {2}'.format(1, 2, 3))
print('a is {2} {0} {1}'.format(1, 2, 3))

print('My name is {} {}'.format('Miyoji', 'Namae'))

print('My name is {first} {last}, Watashi ha {last} {first}'.format(last='Miyoji', first='Namae'))

print(str(1), type)

# f-strings sample
a = 'a'
print(f'a is {a}')

x, y, z = 1, 2, 3
print(f'a is {x}, {y}, {z}')
print(f'a is {z}, {y}, {y}')

name = 'June'
family = 'Sakaki'
print(f'My name is {name} {family}, Watashi ha {family} {name}')