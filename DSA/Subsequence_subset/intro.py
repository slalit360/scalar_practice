def get_subsequence(A):
    # there are total 2^n sub sequences
    # TC : O(n * 2^n)
    final = []
    n = len(A)
    for i in range(1 << n):
        sarr = []
        for j in range(n):
            if i & (1 << j):
                sarr.append(A[j])
        final.append(sarr)
    return final


def check_subsequence_with_sum_k(A, k):
    # You have to find that there is any subsequence exists or not whose sum is equal to B.
    # there are total 2^n sub sequences
    # TC : O(n * 2^n)
    n = len(A)
    for i in range(1 << n):
        summ = 0
        for j in range(n):
            if i & (1 << j):  # check if it jth bit is set of i
                summ += A[j]
        if summ == k:
            return True
    return False


def get_subsets(A):
    # Given a set of distinct integers A, return all possible subsets.
    # A = list(set(A))
    A.sort()

    final = []
    n = len(A)
    for i in range(1 << n):
        sarr = []
        for j in range(n):
            if i & (1 << j):
                sarr.append(A[j])
        final.append(sarr)
    final.sort()
    return final


if __name__ == '__main__':
    print(get_subsequence([1, 2, 3]))
    print(check_subsequence_with_sum_k([1, 2, 3], 2))
    print(get_subsets([1, 2, 3]))
