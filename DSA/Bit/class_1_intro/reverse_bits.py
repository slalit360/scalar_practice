def reverse(A):
    # Reverse the bits of an 32 bit unsigned integer A.
    if A == 0:
        return 0

    bits = ''
    count = 0
    num = A

    result = 0
    n = 32

    while num > 0:
        tmp = num % 2
        bits += str(tmp) # reverse store
        num = num // 2
        count += 1

    for i in range(count):
        if bits[i] == '1':
            result += 2 ** (n - 1)
        n -= 1

    return result


if __name__ == '__main__':
    print(reverse(A=4))  # 536870912
    print(reverse(A=2))  # 1073741824
