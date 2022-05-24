"""
You have given a string A having Uppercase English letters.

You have to find how many times subsequence "AG" is there in the given string.

NOTE: Return the answer modulo 109 + 7 as the answer can be very large.
"""


def get_pair_count_naive(A):
    count = 0
    for j in range(len(A)):
        if A[j] == 'G':
            for i in range(j):
                if A[i] == 'A':
                    count += 1

    return count


def get_pair_count(A):
    n = len(A)
    count = 0
    ans = 0
    for i in range(n):
        if A[i] == 'A':
            count += 1
        if A[i] == 'G':
            ans += count
    return ans


if __name__ == '__main__':
    A = "ABEGAG"
    print(get_pair_count_naive(A))
    print(get_pair_count(A))
