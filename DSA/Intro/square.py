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
        sqrt = mid * mid
        if sqrt == n:
            return mid
        elif sqrt < n:
            low = mid + 1
        else:
            high = mid - 1
    return - 1  # use low -1 for base root required  for 8 root will be 2


def is_no_sum_of_square(n: int) -> bool:
    # O(sqrt(n))
    l = 0
    r = int(sqrt(n))
    while l <= r:
        s = l * l + r * r
        if s > n:
            r -= 1
        elif s < n:
            l += 1
        else:
            return True
    return False

    # for a in range(int(sqrt(n)) + 1):
    #     tmp = a * a
    #     b = int(sqrt(n - tmp))
    #     right_side = int(tmp) + int(b * b)
    #     if right_side == n:
    #         return True
    #     else:
    #         a += 1
    # return False


if __name__ == '__main__':
    for i in range(20):
        # print(get_sqrt_1(N))
        print(i, get_sqrt_2(i))
