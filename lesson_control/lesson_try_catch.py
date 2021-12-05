# 例外処理

l = [1, 2, 3]
i = 5
del l

try:
    l[i]
except IndexError as exc:
    print('Do not worry: {}'.format(exc))
except NameError as exc:
    print(exc)
except Exception as exc:
    print('other: {}'.format(exc))
else:
    # errorが発生しなかった場合に実行される
    print('done')
finally:
    # errorが発生しても実行される
    print('clean up')

print('last')