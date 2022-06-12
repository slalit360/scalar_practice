def pow1(a, n):
    # TC : O(n)
    # SC : O(n)
    if n == 0:
        return 1
    return a * pow(a, n - 1)


def pow(a, n):
    # TC : O(log2 n)
    # SC : O(log2 n)
    if n == 0:
        return 1

    half = pow(a, n // 2)
    res = half * half
    if n & 1 == 1:
        return res * a
    else:
        return res


def main_power(a, n):
    if n < 0:
        return 1 / pow(a, -n)
    else:
        return pow(a, n)


if __name__ == '__main__':
    print(main_power(2, 0))
    print(main_power(2, 2))
    print(main_power(4, -1))
