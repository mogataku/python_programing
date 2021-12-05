# 例外処理の作成

# raise IndexError('test index error')

class UppercaseError(Exception):
    pass

def check():
    words = {'APPLE', 'orange', 'banana'}
    for word in words:
        if word.isupper():
            raise UppercaseError(word)

try:
    check()
except UppercaseError as exc:
    # 独自の例外処理であれば、理解がしやすい
    print('This is my fault, Go next')