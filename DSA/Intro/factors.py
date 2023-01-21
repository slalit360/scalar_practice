import math


def get_factors_divide_by_2(n):
    """
    how many factors we get when divide by 2 to reduce to 1
    TC : O(1)
    """
    return int(math.log2(n))


def print_factors(x):
    """
    print all factors of n
    TC : O(n)
    """
    f = []
    for i in range(1, x + 1):
        if x % i == 0:
            f.append(i)
    return f


def print_factors_new(x):
    """
    print all factors of n
    TC : O(sqrt(n))
    """
    f = []
    for i in range(1, int(math.sqrt(x)) + 1):
        if x % i == 0:
            if x / i == i:  # or i * i == x
                f.append(i)
            else:
                f.append(i)
                f.append(x // i)
    return f


def get_factors_array(A):
    n = max(A) + 1
    B = [0] * n
    B[1] = 1

    for i in range(2, n):
        B[i] = 2

    for k in range(2, n):
        for j in range(k + k, n, k):
            B[j] += 1
    ans = []
    for i in range(len(A)):
        ans.append(B[A[i]])
    return ans


if __name__ == '__main__':
    # print(get_factors_divide_by_2(7))
    A = 4
    # print(print_factors(A))
    # print(sorted(print_factors_new(A)))
    print(get_factors_array([2, 3, 4, 5]))
    print(get_factors_array([8, 9, 10]))
