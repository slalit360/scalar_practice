"""
Q3. Different Bits Sum Pairwise

We define f(X, Y) as the number of different corresponding bits in the binary representation of X and Y.
For example, f(2, 7) = 2, since the binary representation of 2 and 7 are 010 and 111, respectively.
The first and the third bit differ, so f(2, 7) = 2.

You are given an array of N positive integers, A1, A2,..., AN.
Find sum of f(Ai, Aj) for all pairs (i, j) such that 1 ≤ i, j ≤ N. Return the answer modulo 109+7.
"""
import math


# Brute force
# 1. find all pairs
# 2. find diff bits for each pair
# TC : O(n^2 * log(max))

def cntBits(A):
    # TC : O(n * log(max))
    ans = 0
    n = 0
    maxx = -math.inf
    for i in A:
        n += 1
        maxx = max(maxx, i)
    if maxx <= 0:
        return 0
    for i in range(int(math.log2(maxx)) + 1):
        cnt = 0
        for j in A:
            if j & (1 << i):
                cnt += 1
        if cnt == n or cnt == 0:
            ans += 0
        else:
            ans += cnt * (n - cnt)
        ans %= 1000000007
    return ans * 2


if __name__ == '__main__':
    print(cntBits([1, 3, 5]))
