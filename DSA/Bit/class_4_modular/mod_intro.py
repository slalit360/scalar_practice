from time_utility import timeit


@timeit(repeat=1)
def mod_rec(a, n, p):
    if n == 1:
        return a % p
    return (a * mod_rec(a, n - 1, p)) % p


@timeit(repeat=1)
def mod_naive(a, n, p):
    # O(n)
    ans = 1
    for _ in range(n):
        ans = (ans * (a % p)) % p
    return ans


def pow_best(a, n):
    # log2 n
    if n == 0:
        return 1
    half = pow_best(a, n // 2)
    res = half * half
    if n % 2 == 1:
        return res * a
    else:
        return res


@timeit()
def pow_p_best(a, n, p):
    if n == 0:
        return 1
    half = pow_p_best(a, n // 2, p)
    res = (half * half) % p
    if n % 2 == 1:
        return res * (a % p) % p
    else:
        return res


if __name__ == '__main__':
    a = 10
    b = 10000000
    p = 1e9+7
    print(mod_naive(a, b, p))
    # print(mod_rec(a, b, p))
    print(pow_p_best(a, b, p))
    # pow()
