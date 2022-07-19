"""
Q2. Divide Integers

Divide two integers without using multiplication, division and mod operator.
Return the floor of the result of the division.
Also, consider if there can be overflow cases i.e output is greater than INT_MAX, return INT_MAX.
NOTE: INT_MAX = 2^31 - 1
"""


def divide(A, B):
    if A == 0 or B == 0:
        return 0

    sign = 1
    if A < 0:
        sign = -sign
    if B < 0:
        sign = -sign

    B = abs(B)
    A = abs(A)

    ans = 0
    for i in range(31, -1, -1):
        if (B << i) <= A:
            A -= (B << i)
            ans += (1 << i)

    if sign < 0:
        ans = -ans

    INT_MAX = (2 ** 31) - 1
    if ans > INT_MAX:
        return INT_MAX
    return ans


if __name__ == '__main__':
    print(divide(2147483647, 1))
    print(divide(1, 2147483648))
    print(divide(-1, 1))
    print(divide(-1, -1))
    print(divide(0, 1))
    print(divide(4, 2))
