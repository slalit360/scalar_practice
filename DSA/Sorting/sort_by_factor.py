"""
Given an array of size N,
sort them in increasing order of no factors of each element

A = [9, 3, 4, 8, 16, 37, 6, 13, 15]
f = [3, 2, 3, 4,  5,  2, 4,  2,  4]
O = [3, 13, 37, 4, 9, 6, 8, 15, 16]
"""
from functools import cmp_to_key, lru_cache
from math import sqrt

from time_utility import timeit


@lru_cache
def get_count_factors(x):
    # O(sqrt(n))
    count = 0
    for i in range(1, int(sqrt(x)) + 1):
        if x % i == 0:
            if x / i == i:
                count += 1
            else:
                count += 2
    return count


def compare(x, y):
    # O(sqrt(max(A)))
    n1 = get_count_factors(x)
    n2 = get_count_factors(y)
    if n1 > n2:
        return 1
    elif n2 > n1:
        return -1
    else:
        if x > y:
            return 1
        elif y > x:
            return -1
        else:
            return 0


@timeit
def sort_by_factors(Arr):
    # O(n log n * sqrt(max(A)))
    return sorted(Arr, key=cmp_to_key(compare))


if __name__ == '__main__':
    # A = [10] * int(10 ** 6)
    # A = list(range(10**4))
    # sort_by_factors(A)

    A = [9, 3, 4, 8, 16, 37, 6, 13, 15]
    print(sort_by_factors(A))

