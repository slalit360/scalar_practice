"""
Pair Sum - K
Given an array A and K
check if there exist a pair i,j such that A[i] + A[j] == K, where i != j
"""


def check_pair_naive(A, K):
    # TC : O(N^2)
    # SC : O(1)
    n = len(A)
    for i in range(n-1):
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


if __name__ == '__main__':
    A = [7, 4, 10, 2, 5, 16, 3]
    K = 7
    print(check_pair_naive(A, K))
    print(check_pair_hashing_1(A, K))

    # print(check_pair_hashing_exor([1,2,3,4,3,2], 1))