# def comment

def example_func(param1, param2):
    """
    pythonのコメントは、関数の下に記載する
    :param param1:
    :param param2:
    :return:param1
    """
    print(param1, param2)
    return param1;

# 関数のコメントを表示したいとき
print(example_func.__doc__)