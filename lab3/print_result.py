# Здесь должна быть реализация декоратора
def print_result(func_to_decorate): # 1. Функция, которая

    def decorated_func(*args):
        res = func_to_decorate(*args)
        print(func_to_decorate.__name__)
        if isinstance(res, list):
            for i in res:
                print(i)
        elif isinstance(res, dict):
            for k, v in res.items():
                print(k, '=', v)
        else:
            print(res)
        return res

    return decorated_func # 2. возвращает функцию,

@print_result
def test_1():
    return 1


@print_result
def test_2():
    return 'iu5'


@print_result
def test_3():
    return {'a': 1, 'b': 2}


@print_result
def test_4():
    return [1, 2]


if __name__ == '__main__':
    print('!!!!!!!!')
    test_1()
    test_2()
    test_3()
    test_4()
