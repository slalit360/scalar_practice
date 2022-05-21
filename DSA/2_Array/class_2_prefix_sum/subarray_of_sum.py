"""
Subarray with given sum

Given an unsorted array A of size N that contains only non-negative integers, find a continuous sub-array which adds to a given number S.

In case of multiple subarrays, return the subarray which comes first on moving from left to right.

Example 1:

Input:
N = 5, S = 12
A[] = {1,2,3,7,5}
Output: 2 4
Explanation: The sum of elements
from 2nd position to 4th position
is 12.
"""


def subArraySum_naive(arr, n, s):
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
        if summ == s:
            return [i + 1, j + 1]
        elif summ > s:
            i += 1
            j -= 1
        else:
            j += 1
    return [-1]


def subArraySum_optimized(arr, n, s):
    curr_sum = arr[0]
    start = 0
    i = 1

    while i <= n:

        while curr_sum > s and start < i - 1:
            curr_sum -= arr[start]
            start += 1

        if curr_sum == s:
            return [start + 1, i]

        if i < n:
            curr_sum += arr[i]

        i += 1

    return [-1]


if __name__ == '__main__':
    A = [1, 2, 3, 7, 5]
    N = len(A)
    S = 12
    print(subArraySum_naive(A, N, S))
    print(subArraySum_optimized(A, N, S))
