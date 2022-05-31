"""
Sub-array with given sum S

Given an unsorted array A of size N that contains only non-negative integers,
find a continuous sub-array which adds to a given number S.

In case of multiple sub-arrays, return the sub-array which comes first on moving from left to right.

Example 1:

Input:
N = 5, S = 12
A[] = {1,2,3,7,5}
Output: 2 4
Explanation: The sum of elements
from 2nd position to 4th position
is 12.
"""


def get_sub_array_with_sum_S_naive(arr, S):
    n = len(A)

    ps = [0] * n
    ps[0] = arr[0]
    for i in range(1, n):
        ps[i] = ps[i - 1] + arr[i]
    # print(ps)
    i = 0
    j = 0
    while i < n and j < n:
        summ = (ps[j] if j > 0 else 0) - (ps[i - 1] if i > 0 else 0)
        # print(i, j, summ)
        if summ == S:
            return i + 1, j + 1
        elif summ > S:
            i += 1
            j -= 1
        else:
            j += 1
    return [-1]


def get_sub_array_with_sum_S_optimized(arr, S):
    # TC : O(N)
    curr_sum = arr[0]
    start = 0
    i = 1
    n = len(A)
    while i <= n:

        while curr_sum > S and start < i - 1:
            curr_sum -= arr[start]
            start += 1

        if curr_sum == S:
            return start + 1, i

        if i < n:
            curr_sum += arr[i]

        i += 1

    return [-1]


if __name__ == '__main__':
    A = [1, 2, 3, 7, 5]
    S = 12
    print(get_sub_array_with_sum_S_naive(A, S))
    print(get_sub_array_with_sum_S_optimized(A, S))
