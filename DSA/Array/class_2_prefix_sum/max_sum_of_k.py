"""
Max Sum Subarray of size K
Given an array of integers Arr of size N and a number K. Return the maximum sum of a subarray of size K.

Example 1:

Input:
N = 4, K = 2
Arr = [100, 200, 300, 400]
Output:
700
Explanation:
Arr3  + Arr4 =700,
which is maximum.
"""
import math


def maximumSumSubarray(K, Arr, N):
    ps = [Arr[0]]
    for i in range(1, N):
        ps.append(ps[i - 1] + Arr[i])
    # print(ps)
    maxn = -math.inf

    for i in range(N - K + 1):
        end = ps[i + K - 1]
        if i == 0:
            start = 0
        else:
            start = ps[i - 1]
        # print(i, start, end, end - start)
        maxn = max(end - start, maxn)

    return maxn

if __name__ == '__main__':
    A = [100, 200, 300, 400]
    K = 2
    print(maximumSumSubarray(K, A, len(A)))