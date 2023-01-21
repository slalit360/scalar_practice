def rep_sum(n):
    if n <= 0:
        return 0
    return rep_sum(n // 10) + (n % 10)


def magic_no(a):
    if a <= 10:
        if a == 1 or a == 10:
            return 1
        else:
            return 0
    return magic_no(rep_sum(a))


if __name__ == '__main__':
    print(magic_no(1234))
    print(magic_no(2342))
