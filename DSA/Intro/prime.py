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


def prime_no_list(N):
    prime_list = []
    for i in range(N+1):
        if i == 0 or i == 1:
            continue
        else:
            for j in range(2, int(i ** 0.5) + 1):
                if i % j == 0:
                    break
            else:
                prime_list.append(i)
    return prime_list


if __name__ == '__main__':
    print(prime_no_list(7))
    is_prime_2(11)
    is_prime_3(11)
