from time_utility import timeit


# @timeit
def mod_rec(a, n, p):
    if n == 1:
        return a % p
    return (a * mod(a, n - 1, p)) % p


@timeit
def mod(a, n, p):
    ans = 1
    for _ in range(n):
        ans = (ans * (a % p)) % p
    return ans


if __name__ == '__main__':
    print(mod_rec(10 ** 10, 4, 5))
    print(mod(10 ** 10, 4, 5))
