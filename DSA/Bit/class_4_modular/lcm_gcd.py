"""
Least Common Multiple

You are given two non-negative integers, A and B. Find the value of the Least Common Multiple (LCM) of A and B.

LCM of two integers is the smallest positive integer divisible by both.

A = 9
B = 6
18 is the smallest positive integer which is divisible by both 9 (9 * 2 = 18) and 6 (6 * 3 = 18).
"""


def LCM_1(A, B):
    maxx = max(A, B)
    while True:
        if maxx % A == 0 and maxx % B == 0:
            lcm = maxx
            break
        maxx += 1
    return lcm


def LCM_2(A, B):
    gcd = 1
    for i in range(1, min(A, B) + 1):
        if A % i == 0 and B % i == 0:
            gcd = i

    return (A * B) // gcd


if __name__ == '__main__':
    print(LCM_1(9, 6))
    print(LCM_2(9, 6))
