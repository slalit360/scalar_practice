"""
You are given an array of N integers, A1, A2 ,..., AN and an integer K.
Return the of count of distinct numbers in all windows of size K.

Formally, return an array of size N-K+1 where i'th element in this array contains number of distinct elements in
sequence Ai, Ai+1 ,..., Ai+K-1.

NOTE: if K > N, return an empty array.
"""


def dist_no_in_windows_of_size_k(A, K):
    n = len(A)

    hashmap = dict()
    for i in range(K):
        if A[i] in hashmap:
            hashmap[A[i]] += 1
        else:
            hashmap[A[i]] = 1

    ans = [len(hashmap)]
    for i in range(n - K):
        hashmap[A[i]] -= 1
        if hashmap[A[i]] == 0:
            del hashmap[A[i]]

        if A[i + K] in hashmap:
            hashmap[A[i + K]] += 1
        else:
            hashmap[A[i + K]] = 1

        ans.append(len(hashmap))

    return ans


if __name__ == '__main__':
    A = [1, 2, 1, 3, 4, 3]
    K = 3
    print(dist_no_in_windows_of_size_k(A, K))
