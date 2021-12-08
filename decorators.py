def decorator(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)

    return wrapper

def fabric(arg_decor):
    print(f"Я аргумент фабрики {arg_decor}")
    def decorator(fn):
        print(f"Я вызываюсь на момент декорирования {arg_decor}")
        def wrapper(*args, **kwargs):
            return fn(*args, **kwargs)

        return wrapper
    return decorator



@decorator
def test_1(arg1):...


@fabric(444)
def test_2(arg1):...


if __name__ == '__main__':
    test_1(8)
