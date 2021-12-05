# 組み込み関数
import builtins
builtins.print('a')
print(globals())

ranking = {
    'A': 100,
    'B': 45,
    'C': 75
}

print(sorted(ranking))
# 降順に並び替える
print(sorted(ranking, key=ranking.get, reverse=True))