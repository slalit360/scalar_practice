"""
Q1. Beggars Outside Temple

There are A beggars sitting in a row outside a temple. Each beggar initially has an empty pot.
When the devotees come to the temple, they donate some amount of coins to these beggars.
Each devotee gives a fixed amount of coin(according to faith/ability) to some K beggars sitting next to each other.

Given the amount P donated by each devotee to the beggars ranging from L to R index, where 1 <= L <= R <= A,
find out the final amount of money in each beggar's pot at the end of the day,
provided they don't fill their pots by any other means.
For ith devotee B[i][0] = L, B[i][1] = R, B[i][2] = P, Given by the 2D array B
"""


def solve_naive(A, B):
    # TC : O(A * B)
    n = A
    ans = [0] * n
    for l, r, p in B:
        for i in range(l - 1, r):
            ans[i] += p
    return ans


def solve(A, B):
    # TC : O(A)
    ans = [0] * A

    for l, r, p in B:
        ans[l - 1] += p
        if r < A:
            ans[r] -= p

    sum = 0
    for i in range(A):
        sum += ans[i]
        ans[i] = sum

    return ans


if __name__ == '__main__':
    A = 5
    B = [[1, 2, 10], [2, 3, 20], [2, 5, 25]]
    print(solve_naive(A, B))
    print(solve(A, B))
