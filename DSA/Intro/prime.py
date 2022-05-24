def is_prime_1(n):
    """
    check if given n is prime or not
    TC : o(n) # n
    """
    if n == 1:
        print(f"{n} is not prime number")
        return
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    if count == 2:
        print(f"{n} is prime number")
    else:
        print(f"{n} is not prime number")


def is_prime_2(n):
    """
    check if given n is prime or not
    TC : o(n) # n-1
    """
    for i in range(2, n):
        if n % i == 0:
            print(f"{n} is not prime number")
            return
    if n != 1:
        print(f"{n} is prime number")
    else:
        print(f"{n} is not prime number")


def is_prime_3(n):
    """
    check if given n is prime or not
    TC : o(sqrt(n)) # sqrt(n)
    """
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            print(f"{n} is not prime number")
            return
    if n != 1:
        print(f"{n} is prime number")
    else:
        print(f"{n} is not prime number")


if __name__ == '__main__':
    is_prime_1(11)
    is_prime_2(11)
    is_prime_3(11)
