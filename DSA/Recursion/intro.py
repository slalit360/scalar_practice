def factorial(n):
    if n <= 0:
        return 1
    return factorial(n - 1) * n


def fibonacci(n):
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def check_palindrome(a, i, j):
    if i >= j:
        return 1
    elif a[i] == a[j]:
        return check_palindrome(a, i + 1, j - 1)
    return 0


def rec_sum(n):
    if n == 0:
        return 0
    return (n % 10) + rec_sum(n // 10)


def sum_of_digit(n):
    if n == 0:
        return 0
    return n % 10 + sum(n // 10)


if __name__ == '__main__':
    # print(factorial(5))
    # print(fibonacci(4))
    # print(check_palindrome("madam", 0, 4))
    # print(check_palindrome("madan", 0, 4))
    # print(check_palindrome("naan", 0, 3))
    # print(check_palindrome("naam", 0, 3))
    # print(rec_sum(6))
    print(sum(1234))
