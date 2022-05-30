"""
find LCM and GCD of given two numbers

a x b = LCM(a, b) * GCD (a, b)

LCM(a, b) = (a x b) / GCD(a, b)

"""


def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


def lcm(a, b):
    return (a * b) // gcd(a, b)


if __name__ == '__main__':
    print(gcd(12, 6))
    print(lcm(12, 6))
