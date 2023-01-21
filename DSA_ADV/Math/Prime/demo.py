def primesum(A):
    # use smallest prime factorization
    if A == 4:
        return [2, 2]

    # build seive of eratosthenes
    sieve = [1] * (A + 1)
    sieve[0] = 0
    sieve[1] = 0

    i = 2
    while i * i <= A:
        if sieve[i] == 1:
            j = i * i
            while j <= A:
                sieve[j] = 0
                j += i
        i += 1

    # find pair with sum
    for i in range(2, A + 1):
        if sieve[i] == 1 and sieve[A - i] == 1:
            return [i, A - i]
    return []


if __name__ == '__main__':
    print(primesum(10))
