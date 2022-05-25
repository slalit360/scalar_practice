from time_utility import timeit

n_obs = 10 ** 6


@timeit(repeat=n_obs)
def check_palindrome_python(A):
    return A == A[::-1]


@timeit(repeat=n_obs)
def check_palindrome(A):
    # O(n)
    i = 0
    n = len(A)
    j = n - 1

    while i < j:
        if A[i] != A[j]:
            return False
        i += 1
        j -= 1

    return True


if __name__ == '__main__':
    print(check_palindrome_python("12345678987654321"))
    print(check_palindrome("12345678987654321"))
