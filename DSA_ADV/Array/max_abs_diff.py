"""
You are given an array of N integers, A1, A2, .... AN.

Return the maximum value of f(i, j) for all 1 ≤ i, j ≤ N.
f(i, j) is defined as |A[i] - A[j]| + |i - j|, where |x| denotes absolute value of x.
"""
import math


def maxArr(A):
    x_max, y_max = -math.inf, -math.inf
    x_min, y_min = math.inf, math.inf

    n = len(A)

    for i in range(n):
        x_max = max(x_max, A[i] + i)
        x_min = min(x_min, A[i] + i)

        y_max = max(y_max, A[i] - i)
        y_min = min(y_min, A[i] - i)

    return max(x_max - x_min, y_max - y_min)


if __name__ == '__main__':
    Arr = [1, 3, -1]
    print(maxArr(Arr))
