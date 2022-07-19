"""
Q2. Count Total Set Bits

Given a positive integer A, 
the task is to count the total number of set bits in the binary representation of all the numbers from 1 to A.
Return the count modulo 109 + 7.
"""
import math


def totalSetBits(A):
    mod = 1000000007
    # # TC : O(n * log(max(A)))
    # ans = 0
    # for i in range(1, A+1):
    #     n = i
    #     while n:
    #         if n & 1:
    #             ans += 1
    #         n >>= 1
    # return ans % mod

    bits = int(math.log(A, 2)) + 1
    mod = 1000000007
    no_of_1 = 0
    for i in range(bits, 0, -1):
        no_of_1 += (A // (1 << i)) * (1 << (i - 1))
        if A // (1 << (i - 1)) & 1:
            no_of_1 += ((A % (1 << (i - 1))) + 1)
    return no_of_1 % mod


if __name__ == '__main__':
    print(totalSetBits(3))
