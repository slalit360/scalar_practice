"""
Given an array A of non-negative integers, arrange them such that they form the largest number.
Note: The result may be very large, so you need to return a string instead of an integer.

Example Input

A = [3, 30, 34, 5, 9]
Output 1: "9534330"

A = [2, 3, 9, 0]
Output 2: "9320"
"""

from functools import cmp_to_key


def compare(a, b):
    # log10(max(A))
    a = str(a) + str(b)
    b = str(b) + str(a)
    if a > b:
        return 1
    elif b > a:
        return -1
    else:
        return 0


def get_largest_no(Arr):
    # n log n
    return int("".join(map(str, sorted(Arr, key=cmp_to_key(compare), reverse=True))))


if __name__ == '__main__':
    A = [3, 30, 34, 5, 9]
    print(get_largest_no(A))
