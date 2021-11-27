# for break continue
some_list = [1, 2, 3, 4, 5]

i = 0
while i < len(some_list):
    print(some_list[i])
    i += 1

some_list2 = [1, 2, 3, 4, 5]
for i in some_list2:
    print(i)
# jsのforeach

for s in 'qweasd':
    if s == 'a':
        continue
    print(s)

for word in ['My', 'name', 'is', 'Jone']:
    if word == 'is':
        break
    print(word)

# for else
for fruit in ['apple', 'banana', 'orange']:
    if fruit == 'banana':
        print('stop eating')
        break
    print(fruit)
else:
    print('I ate all!')