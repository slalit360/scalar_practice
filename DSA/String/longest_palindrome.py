"""
Given a string A of size N, find and return the longest palindromic substring in A.

Substring of string A is A[i...j] where 0 <= i <= j < len(A)

Palindrome string:
A string which reads the same backwards. More formally, A is palindrome if reverse(A) = A.

In Case of conflict, return the substring which occurs first ( with the least starting index).
"""


def get_longest_palindrome_length(A):
    # O(n^2)
    max_length = 1
    n = len(A)

    for i in range(n):
        # odd length cases
        p1 = i - 1
        p2 = i + 1
        while p1 >= 0 and p2 < n:
            if A[p1] == A[p2]:
                max_length = max(max_length, p2 - p1 + 1)
                p1 -= 1
                p2 += 1
            else:
                break
        # even length cases
        p1 = i
        p2 = i + 1
        while p1 >= 0 and p2 < n:
            if A[p1] == A[p2]:
                max_length = max(max_length, p2 - p1 + 1)
                p1 -= 1
                p2 += 1
            else:
                break
    return max_length


def max_size_palindrome(A):
    # O(n^2)
    max_length = 1
    n = len(A)
    ans = None

    for i in range(n):
        # odd length cases
        p1 = i - 1
        p2 = i + 1
        while p1 >= 0 and p2 < n:
            if A[p1] == A[p2]:
                if p2 - p1 + 1 > max_length:
                    ans = A[p1:p2 + 1]
                    max_length = p2 - p1 + 1
                p1 -= 1
                p2 += 1
            else:
                break
        # even length cases
        p1 = i
        p2 = i + 1
        while p1 >= 0 and p2 < n:
            if A[p1] == A[p2]:
                if p2 - p1 + 1 > max_length:
                    ans = A[p1:p2 + 1]
                    max_length = p2 - p1 + 1
                p1 -= 1
                p2 += 1
            else:
                break
    if ans:
        return "".join(ans)  # , max_length
    else:
        return "".join(A[:max_length])  # , max_length,


if __name__ == '__main__':
    print(max_size_palindrome(list("abccbaxy")))
    print(max_size_palindrome(list("abaxabaxabb")))
    print(max_size_palindrome(list("ac")))
    print(max_size_palindrome(list("abb")))
    print(max_size_palindrome(list("a")))
