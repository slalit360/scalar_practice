"""
You are given a binary string A(i.e., with characters 0 and 1) consisting of characters A1, A2, ..., AN.
In a single operation, you can choose two indices, L and R, such that 1 ≤ L ≤ R ≤ N and flip the characters AL, AL+1, ..., AR.
By flipping, we mean changing character 0 to 1 and vice-versa.

Your aim is to perform ATMOST one operation such that in the final string number of 1s is maximized.

If you don't want to perform the operation, return an empty array. Else, return an array consisting of two elements denoting L and R.
If there are multiple solutions, return the lexicographically smallest pair of L and R.

NOTE: Pair (a, b) is lexicographically smaller than pair (c, d) if a < c or, if a == c and b < d.
"""
import math


def flip(A):
    ans = []
    og_1s = 0
    n = 0

    for i in A:
        if i == '1':
            og_1s += 1
        n += 1
    if n == og_1s:
        return []

    maxx = 0
    for i in range(n):
        cnt_0 = 0
        cnt_1 = 0
        for j in range(i, n):
            if A[j] == '0':
                cnt_0 += 1
            else:
                cnt_1 += 1

            if maxx < (og_1s - cnt_1 + cnt_0):
                ans = [i + 1, j + 1]
                maxx = og_1s - cnt_1 + cnt_0
    return ans


def flip_bin(Arr):
    og_1s = 0
    n = 0

    curr_sum = 0
    max_sum = -math.inf
    s, e, start, end = 0, 0, -1, -1

    for i, v in enumerate(Arr):
        if Arr[i] == '1':
            val = -1
            og_1s += 1
        else:
            val = 1

        if curr_sum + val >= 0:
            curr_sum += val
            e = i
        else:
            curr_sum = 0
            s = i + 1

        if curr_sum > max_sum:
            max_sum = curr_sum
            start = s
            end = e

        n += 1

    if start == -1 or n == og_1s:
        return []

    print(Arr[start: end+1])
    return [start+1, end+1]


if __name__ == '__main__':
    print(flip_bin("0000"))
    print(flip_bin("1111"))
    print(flip_bin("10010100"))
    print(flip_bin("1101010001"))
