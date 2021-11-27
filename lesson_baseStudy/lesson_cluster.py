# cluster
a = {1, 2, 3, 4, 4, 4, 5, 6, 7, 7, 7}
print(a)
# 重複は表示しない
b = {1, 2, 10}
print(a - b)
print(a & b)
print(a | b)
print(a ^ b)

# clusterのメソッド
s = {1, 2, 3, 4, 5}
# 追加削除はできるが並び替えはできない
# 空の場合は、{}ではなく()が表示される

# clusterの使い道
Taro_friends = {'A', 'B', 'D'}
A_friends = {'C', 'D', 'E', 'F'}
print(Taro_friends & A_friends)

f = ['apple', 'banana', 'apple', 'banana']
kind = set(f)
# 種類のみを取得
print(kind)