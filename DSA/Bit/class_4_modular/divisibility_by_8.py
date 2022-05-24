"""
Divisibility by 8
You are given a number A in the form of a string. Check if the number is divisible by eight or not.

Return 1 if it is divisible by eight else, return 0.
"""


def divisibility_by_8(A):
    n = len(A)
    if n >= 3:
        A = A[-3:]
    if int(A) % 8 == 0:
        return 1 # divisible by 8
    else:
        return 0


if __name__ == '__main__':
    print(divisibility_by_8("123"))