from math import sqrt


def get_sqrt_1(n):
    """
    given perfect square , find sqrt of no
    TC : O(n)
    """
    for i in range(1, int(sqrt(n)) + 1):
        if i * i == n:
            return i
    return -1


def get_sqrt_2(n):
    """
    given perfect square , find sqrt of no
    TC : O(log n)
    """
    low = 1
    high = n

    while low <= high:
        mid = (low + high) // 2
        if mid * mid > n:
            high = mid - 1
        elif mid * mid < n:
            low = mid + 1
        else:
            return mid
    return -1


if __name__ == '__main__':
    N = 16
    print(get_sqrt_1(N))
    print(get_sqrt_2(N))
