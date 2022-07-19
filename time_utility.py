import functools
from time import time
from typing import Optional


def timeit(repeat: Optional[int] = 1):
    def timeit1(func):
        @functools.wraps(func)
        def wrap_func(*args, **kwargs):
            t1 = time()
            for _ in range(repeat):
                result = func(*args, **kwargs)
            t2 = time()
            print(f'Function {func.__name__!r} executed in {(t2 - t1):.8f}s')
            return result

        return wrap_func
    return timeit1