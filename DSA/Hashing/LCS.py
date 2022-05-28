"""
Q3. Largest Continuous Sequence Zero Sum

Given an array A of N integers.

Find the largest continuous sequence in a array which sums to zero.
"""


def LCS_zero(A):
    maxlcs, j, k = 0, -1, -1
    d = {0: -1}
    summ = 0
    for i in range(len(A)):
        summ += A[i]
        if summ in d:
            if maxlcs < i - d[summ]:
                maxlcs = i - d[summ]
                j = d[summ] + 1
                k = i
        else:
            d[summ] = i
    return A[j: k+1] if maxlcs else []


if __name__ == '__main__':
    print(LCS_zero([1, 2, -2, 4, -4]))
