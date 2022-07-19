"""
Q3. Smallest XOR

Given two integers A and B,
find a number X such that A xor X is minimum possible, and the number of set bits in X equals B.
"""


def solve(A, B):
    X = A
    count_set_bits = 0
    while X:
        if X & 1:
            count_set_bits += 1
        X = X >> 1
    if count_set_bits == B:
        return A
    elif count_set_bits < B:
        Y = A
        i = 0
        while count_set_bits < B:
            if A & (1 << i):
                i += 1
            else:
                Y |= (1 << i)
                i += 1
                count_set_bits += 1
        return Y
    else:
        Z = A
        j = count_set_bits
        i = 0
        while B < j:
            if A & (1 << i):
                Z ^= (1 << i)
                j -= 1
            i += 1
        return Z


if __name__ == '__main__':
    print(solve(15, 2))
