"""
Excel Column Number
Given a column title as appears in an Excel sheet, return its corresponding column number.
AB -> 28
ABCD -> 19010

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28

"""


def titleToNumber(A):
    n = len(A)
    ans = 0

    # char_dict = {v:k+1 for k, v in enumerate(string.ascii_uppercase)}

    # for i in A:
    #     ans += char_dict[i] * 26**(n-1)
    #     n -= 1

    A = A[::-1]

    for i in range(n):
        ans += (ord(A[i]) - ord('A') + 1) * (26 ** (i))
    return ans


