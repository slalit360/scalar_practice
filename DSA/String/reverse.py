from typing import List


def reverse(A: List, i, j):
    # O(n)
    while i < j:
        A[i], A[j] = A[j], A[i]
        i += 1
        j -= 1
    return A


def reverse_word_by_word_python(A):
    return " ".join(A.strip().split(" ")[::-1])


def reverse_word_by_word(A: List):
    # O(n^2)
    n = len(A)
    A = reverse(A, 0, n - 1)
    i = 0
    j = 0
    while i <= n-1:
        if A[i] == ' ':
            A = reverse(A, j, i - 1)
            j = i + 1
        elif i == n-1:
            A = reverse(A, j, i)
            j = i + 1
        i += 1

    return A


if __name__ == '__main__':
    print("".join(reverse_word_by_word(list("my name is lalit"))))
