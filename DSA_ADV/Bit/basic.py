"""
Write a function that takes an integer and returns the number of 1 bits it has.
"""


def numSetBits(A):
    import math
    cnt = 0
    for i in range(int(math.log2(A))):
        if A & (1 << i):
            cnt += 1
    return cnt + 1


"""
Reverse the bits of an 32 bit unsigned integer A.
"""


def reverse(A):
    ans = 0
    m = 31
    while A:
        if A & 1:
            ans += (1 << m)
        m -= 1
        A = A >> 1
    return ans


if __name__ == '__main__':
    print(numSetBits(3))
    print(reverse(3))
    print(reverse(0))