# tupple
t = (1, 2, 3, 4, 1, 2)
print(t)
# リストよりもサポートが少ない
# t[0] = 100

print(t[0])
print(t.count(1))
print(t[2:])

t = (t , t)
print(t)
# t[0] = [1]
print(t[0][0])
# t[0][0] = 100
print(t)
print(type(t))

# 一つだけでもtuppleになるため注意が必要
t = 1,
print(type(t))

# tuppleを使う場合は「,]を忘れないようにする


num_tupple = (10, 20)
print(num_tupple)

# アンパッキング
x, y = num_tupple
print(x)
print(y)

# 変数の入れ替え
a, b = 100, 200
print(a, b)
a, b = b, a
print(b, a)

# 実施例
chose_from_two = ('A', 'B', 'C')
answer = []
answer.append('A')
answer.append('B')

print(chose_from_two)
print(answer)