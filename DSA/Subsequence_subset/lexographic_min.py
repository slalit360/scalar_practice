"""
Given a string A, and find out the lexicographically minimum subsequence from it of size >= 2. Can you help him?

A string a is lexicographically smaller than string b, if the first different letter in a and b is smaller in a.

"abc" is lexicographically smaller than "acc" as the first different letter is 'b' and 'c' which is smaller in "abc".
"""


def lex_min_naive(A):
    # TC : O(n * 2^n)
    def is_set(s, k):
        return s & (1 << k)

    n = len(A)
    ans = "z" * n
    for i in range(2 ** n):
        m = ""
        for j in range(n):
            if is_set(i, j):
                m += A[j]
        if len(m) >= 2:
            ans = min(ans, m)
    return ans


def lex_min(A):
    # TC : O(n)
    n = len(A)
    minchar = 'z'

    for i in range(n - 1):
        minchar = min(minchar, A[i])
    idx = A.index(minchar)

    minchar1 = 'z'
    for i in range(idx + 1, n):
        minchar1 = min(minchar1, A[i])

    return minchar + minchar1


def find_sub_seq(A, B):
    """
    Given two strings A and B, find if A is a subsequence of B. Return "YES" if A is a subsequence of B, else "NO".
    TC : O(n)
    """
    na = len(A)
    nb = len(B)

    i = 0
    j = 0
    while i < nb:
        if A[j] == B[i]:
            if j == na - 1:
                return "YES"
            j += 1
        i += 1
    return "NO"


if __name__ == '__main__':
    A = "ksdjgha"  # "abcdsfhjagj"
    print(lex_min_naive(A))
    print(lex_min(A))

    print(find_sub_seq(A="bit", B="dfbkjijgbbiihbmmt"))

