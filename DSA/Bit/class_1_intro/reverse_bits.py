def reverse(A):
    # Reverse the bits of an 32 bit unsigned integer A.
    if A == 0:
        return 0

    result = 0
    n = 31

    while A > 0:
        if A % 2 == 1: # reverse store
            result += 2 ** (n)
        A = A // 2
        n -= 1

    return result


if __name__ == '__main__':
    print(reverse(A=4))  # 536870912
    print(reverse(A=2))  # 1073741824
