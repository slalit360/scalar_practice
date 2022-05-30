"""
Q3. COLORFUL Number

Given a number A, find if it is COLORFUL number or not.
If number A is a COLORFUL number return 1 else, return 0.

What is a COLORFUL Number:
A number can be broken into different contiguous sub-subsequence parts.
Suppose, a number 3245 can be broken into parts like 3 2 4 5 32 24 45 324 245.
And this number is a COLORFUL number, since product of every digit of a contiguous subsequence is different.

Constraint :
1 <= A <= 2 * 109
"""

from functools import reduce


def colorful1(A):
    # TC : O(n^2)
    # SC : O(no. of sub-array)

    # num to array or num to str
    # form sub array's of k <- 1 to n-1
    # find product of all sub array in hashmap/set
    # if product already exist return 0 else return 1

    A = str(A)  # list(map(int, str(A)))
    n = len(A)
    k = 1
    i = 0

    hashset = set()
    while k <= n:
        if i < n - k + 1:
            tmp = A[i:i + k]
            p = str(reduce((lambda x, y: int(x) * int(y)), tmp))
            if p in hashset:
                return 0
            else:
                hashset.add(p)
        i += 1
        if i == n:
            i = 0
            k += 1
    return 1


def findProd(A):
    ret = 1
    for a in A:
        ret *= int(a)
    return str(ret)


def colorful(A):
    numbers = dict()
    strA = str(A)
    # for a in strA:
    #     if a in numbers:
    #         return 0
    #     else:
    #         numbers[a] = 1
    n = len(strA)
    for i in range(1, n + 1):
        for j in range(n - i + 1):
            num = strA[j: j + i]
            ret = findProd(num)
            if ret in numbers:
                return 0
            else:
                numbers[ret] = 1
    return 1


if __name__ == '__main__':
    print(colorful1(1235), colorful(1235))
    print(colorful1(23), colorful(23))
    print(colorful1(236), colorful1(236))
