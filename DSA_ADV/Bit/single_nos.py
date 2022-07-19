# for these problems we could use following approaches:-
# 1. two nested for loop with O(n^2)
# 2. using freq hashmap with O(n)
# 3. sort and then count freq O(n * log n)
# 4. below mentioned approaches

"""
Q1. Single Number I

Given an array of integers A, every element appears twice except for one. Find that integer that occurs once.

NOTE: Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
"""
import math


def single_no_1(A):
    # TC : O(n)
    ans = 0
    for i in A:
        ans ^= i
    return ans


"""
Q2. Single Number II

Given an array of integers, every element appears thrice except for one, which occurs once.
Find that element that does not appear thrice.

NOTE: Your algorithm should have a linear runtime complexity.
Could you implement it without using extra memory?
"""


def single_no_2(A):
    # TC : O(n * log(max(A)) )
    xor = 0
    maxx = -math.inf
    n = 0
    for i in A:
        xor ^= i
        maxx = max(maxx, i)
        n += 1

    ans = 0
    for i in range(int(math.log2(maxx)) + 1):
        cnt_of_1s = 0
        for j in A:
            if j & (1 << i):
                cnt_of_1s += 1
        if cnt_of_1s % 3:  # if for all no n times except one
            ans = ans | (1 << i)
    return ans


"""
Q3. Single Number III

Given an array of positive integers A, two integers appear only once, and all the other integers appear twice.
Find the two integers that appear only once.
"""


def single_no_3(A):
    # TC : O(n * log(xor) )
    xor = 0
    for i in A:
        xor ^= i

    # check for LSB set bit position
    idx = 0
    for i in range(int(math.log2(xor))):
        if xor & (1 << i):  # check bit
            idx = i
            break
    a = 0
    b = 0
    # check mask set bit with every element (separates numbers into two groups)
    for i in A:
        # check m
        if i & (1 << idx) != 0:
            a ^= i
        else:
            b ^= i
    return (b, a) if a > b else (a, b)


if __name__ == '__main__':
    A = [1, 1, 2, 2, 5, 6, 6]
    print(single_no_1(A))
    A = [1, 1, 1, 2, 2, 2, 3]
    print(single_no_2(A))
    A = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3]
    print(single_no_2(A))
    A = [1, 1, 4, 6, 6, 5]
    print(single_no_3(A))
