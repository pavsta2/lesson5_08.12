import time
from collections import OrderedDict
from functools import lru_cache

def cache(maxsize=3):
    def decorat_cache(fn):
        dict_cache = OrderedDict()

        def wrapper(*args):
            if args not in dict_cache:
                if dict_cache == maxsize:
                    dict_cache.popitem(last=False)
                result = fn(*args)
                dict_cache[args] = result

            return dict_cache[args]

        return wrapper

    return decorat_cache


@cache(3)
def my_sleep1():
    time.sleep(3)

@lru_cache(maxsize=None)
def my_sleep2():
    time.sleep(3)

if __name__ == '__main__':
    t0 = time.time()

    print(my_sleep1())
    print(my_sleep1())

    print(time.time() - t0)
