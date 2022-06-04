"""
Given an array of size N, find the majority element. The majority element is the element that appears more than floor(n/2) times.
You may assume that the array is non-empty and the majority element always exists in the array.

"""


def get_majority_element_1(A):
    # with hashmap
    n = len(A)
    ans = 0
    d = {}
    for i in A:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
        if d[i] > (n // 2):
            ans = i
    return ans


def get_majority_element_2(A):
    # with sorting
    n = len(A)
    ans = 0
    if n == 1:
        return A[0]
    A = sorted(A)
    ans = A[n // 2]
    return ans


def get_majority_element(A):
    # with moore algo
    majority_idx = 0
    count = 1
    n = len(A)
    for i in range(1, n):
        if A[majority_idx] == A[i]:
            count += 1
        else:
            count -= 1
        if count == 0:
            majority_idx = i
            count = 1
    ret = A[majority_idx]
    count = 0
    for a in A:
        if a == ret:
            count += 1
    if count >= n / 2:
        return ret
    return -1


if __name__ == '__main__':
    print(get_majority_element([1, 2, 2, 3, 5, 2, 2]))
