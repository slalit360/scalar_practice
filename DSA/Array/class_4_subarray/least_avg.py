"""
Q3. Subarray with least average

Problem Description

    Given an array of size N, find the subarray of size K with the least average.
"""

import math


def solve(A, B):
    # B is allowed size
    k = B
    n = len(A)
    avg = math.inf

    ps = [A[0]]
    for i in range(1, n):
        ps.append(ps[i - 1] + A[i])

    j = 0
    for i in range(n - k + 1):
        if i == 0:
            tmp = ps[k - 1] / k
        else:
            tmp = (ps[i + k - 1] - ps[i - 1]) / k
        if tmp < avg:
            avg = tmp
            j = i
    return j


if __name__ == '__main__':
    A = [3, 7, 90, 20, 10, 50, 40]
    B = 3
    print(solve(A, B))
    A = [3, 7, 5, 20, -10, 0, 12]
    B = 2
    print(solve(A, B))
