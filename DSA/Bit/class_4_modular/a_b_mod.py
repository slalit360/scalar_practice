"""
Given two integers A and B, find the greatest possible positive integer M, such that A % M = B % M.

Input 1:
A = 1
B = 2
Output 1:
1
1 is the largest value of M such that A % M == B % M.

Input 2:
A = 5
B = 10
Output 2:
5
For M = 5, A % M = 0 and B % M = 0.
No value greater than M = 5, satisfies the condition.
"""


def ab_mod_1(A, B):
    if A > B:
        tmp = A - B
    else:
        tmp = B - A

    for i in range(tmp, 0, -1):
        if A % tmp == B % tmp:
            return tmp


def ab_mod_2(A, B):
    return abs(A - B)


if __name__ == '__main__':
    print(ab_mod_1(5, 10))
    print(ab_mod_2(5, 10))
