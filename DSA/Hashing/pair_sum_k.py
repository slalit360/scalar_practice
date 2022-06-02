"""
Pair Sum - K
Given an array A and K
check if there exist a pair i,j such that A[i] + A[j] == K, where i != j
"""


def check_pair_naive(A, K):
    # TC : O(N^2)
    # SC : O(1)
    n = len(A)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if A[i] + A[j] == K:
                return True, i, j
    return False


def check_pair_hashing_1(A, K):
    # TC : O(N)
    # SC : O(N)
    n = len(A)
    hashset = set()
    for i in range(n):
        if K - A[i] in hashset:
            return True
        hashset.add(A[i])
    return False


def twoSum(A, B):
    # TC : O(N)
    # SC : O(N)
    hashmap = dict()
    for j in range(len(A)):
        if B - A[j] in hashmap:
            i = hashmap[B - A[j]]
            print(i + 1, j + 1)
            # return [i + 1, j + 1]
        else:
            if A[j] not in hashmap:
                hashmap[A[j]] = j
    return []

    # hashDict = dict()
    # n = len(A)
    # for i in range(n):
    #     if A[i] in hashDict:
    #         return [hashDict[A[i]] + 1, i + 1]
    #     elif B - A[i] not in hashDict:
    #         hashDict[B - A[i]] = i
    # return []


def diffPossible(A, K):
    """
    Given an array A of integers and another non negative integer k,
    find if there exists 2 indices i and j such that A[i] - A[j] = k, i != j.
    """

    # n = len(A)
    # for i in range(n):
    #     for j in range(i, n):
    #         if i != j and abs(A[j] - A[i]) == B:
    #             return 1
    # return 0

    A.sort()
    hashset = set()

    for i, a in enumerate(A):
        if a - K in hashset:
            return 1
        else:
            hashset.add(a)

    return 0


if __name__ == '__main__':
    # A = [4, 7, -4, 2, 2, 2, 3, -5, -3, 9, -4, 9, -7, 7, -1, 9, 9, 4, 1, -4, -2, 3, -3, -5, 4, -7, 7, 9, -4, 4, -8]
    # A = [7, 4, 10, 2, 5, 16, 3]
    # K = -3
    # K = 7

    # print(check_pair_naive(A, K), "\n")
    # print(check_pair_hashing_1(A, K), "\n")
    # print(twoSum(A, K))
    print(diffPossible([11, 85, 100, 44, 3, 32, 96, 72, 93, 76, 67, 93, 63, 5, 10, 45, 99, 35, 13], 60)) # 1
    print(diffPossible([1, 3, 2], 0)) # 0
    print(diffPossible([ 77, 28, 19, 21, 67, 15, 53, 25, 82, 52, 8, 94, 50, 30, 37, 39, 9, 43, 35, 48, 82, 53, 16, 20, 13, 95, 18, 67, 77, 12, 93, 0 ],
                       53)) # 1
