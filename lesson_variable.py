# variable 変数の型変換が簡単になっている 変数は数字から始めることができない
num = 1
name = 'Mika'

print(num, type(num))
print(name, type(name))

num = name

print(num, type(name))