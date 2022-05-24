"""
Find nth Magic Number

Given an integer A, find and return the Ath magic number.

A magic number is defined as a number that can be expressed as a power of 5 or a sum of unique powers of 5.

First few magic numbers are 5, 25, 30(5 + 25), 125, 130(125 + 5), ….
"""


def nth_magic_no(A):
    # O(log n)
    ans = 0
    poww = 5

    while A > 0:
        ans += (A & 1) * poww  # (5 ** n)
        poww *= 5
        # n += 1
        A = A >> 1
        # print(ans)
    return ans


if __name__ == '__main__':
    print(nth_magic_no(5))