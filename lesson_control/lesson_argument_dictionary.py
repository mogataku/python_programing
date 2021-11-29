# argument dictionary
def menu(entree='beef', drink='wine'):
    print(entree, drink)

menu(entree='meet', drink='orange juice')

def menu2(**kwargs):
    print(kwargs)
    for k, v in kwargs.items():
        print(k, v)

menu2(entree='meet', drink='orange juice')
d = {
    'entree': 'beef',
    'drink': 'ice tea',
    'desert': 'ice cream'
}
menu2(**d)

# *の数の順に引数を指定すること
def menu3(food, *args, **kwards):
    print(food)
    print(args)
    print(kwards)

# menu3()