"""
Given an array A, find the size of the smallest subarray such that it contains at least one occurrence of the maximum value of the array

and at least one occurrence of the minimum value of the array.
"""
import math


def get_smallest_min_max_array_len_naive(A):
    # TC : O(n^2)
    # SC : O(1)
    n = len(A)
    maxn = max(A)
    minn = min(A)

    ans = math.inf
    for i in range(n):
        if A[i] == minn:
            for j in range(i, -1, -1):
                if A[j] == maxn:
                    ans = min(ans, i - j + 1)

        if A[i] == maxn:
            for j in range(i, -1, -1):
                if A[j] == minn:
                    ans = min(ans, i - j + 1)
    return ans


def get_smallest_min_max_array_len(A):
    # TC : O(n)
    # SC : O(1)
    ans = math.inf

    latest_max = -1
    latest_min = -1

    maxn = max(A)
    minn = min(A)

    for i in range(len(A)):
        if A[i] == maxn:
            if latest_min != -1:
                ans = min(ans, i - latest_min + 1)
            latest_max = i

        if A[i] == minn:
            if latest_max != -1:
                ans = min(ans, i - latest_max + 1)
            latest_min = i

    return ans


if __name__ == '__main__':
    A = [1, 2, 3, 1, 3, 4, 6, 4, 6, 3]
    print(get_smallest_min_max_array_len_naive(A))
    print(get_smallest_min_max_array_len(A))
