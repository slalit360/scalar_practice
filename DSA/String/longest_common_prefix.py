"""
Given the array of strings A, you need to find the longest string S, which is the prefix of ALL the strings in the array.

The longest common prefix for a pair of strings S1 and S2 is the longest string S which is the prefix of both S1 and S2.

Example: the longest common prefix of "abcdefgh" and "abcefgh" is "abc".
"""

import math


def common_prefix(A, B):
    # TC : O(min(len(A), len(B)))
    l = min(len(A), len(B))
    ans = ""
    for i in range(l):
        if A[i] != B[i]:
            break
        else:
            ans += A[i]
    return ans


def longest_comm_prefix_naive(A):
    # compare prefix sum way
    # TC : O(k) : sum of length of all strings
    n = len(A)
    com_pre = [A[0]]
    for i in range(1, n):
        com_pre.append(common_prefix(com_pre[i - 1], A[i]))
    return com_pre[n - 1]


def longest_common_prefix(A):
    # O(m * n) where n is total no of strings, m is length of smallest string
    # SC : O(1)
    n = len(A)
    if n <= 1:
        return A[0]
    else:
        ans = ""
        min_l = math.inf
        for i in A:
            min_l = min(min_l, len(i))

        for j in range(min_l):
            flag = True
            for i in range(n - 1):
                if A[i][j] == A[i + 1][j]:
                    pass
                else:
                    flag = False
                    break
            if not flag:
                break
            else:
                ans += A[0][j]
        return ans


if __name__ == '__main__':
    print(longest_comm_prefix_naive(["abc", "ab", "a"]))
    print(longest_comm_prefix_naive(["abcd", "abd", "abcd"]))
    print(longest_comm_prefix_naive(["abc", "ab", "a"]))
