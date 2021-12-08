from functools import wraps
from typing import Optional

def decorator(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)

    # wrapper.__name__ = fn.__name__
    # wrapper.__doc__ = fn.__doc__
    return wrapper

@decorator
def test(arg1: str, arg2) -> Optional[list]: # ВСПОМНИТЬ ЭТО!!!!
    """
    Общее описание функции
    Примеры кода
    :param arg1: Описание параметра
    :param arg2:
    :return: Что возвращает
    """
    ...

@decorator
def test2(arg1, arg2):
    """Краткое поисание в одну строку"""
    ...

print("darfaf")

if __name__ == '__main__':
    print(test.__name__)
    print(test.__doc__)

    help(test)