def lowercase(A):
    # return [x.lower() for x in A]
    r = ""
    for i in A:
        if 65 <= ord(i) <= 90:
            r += chr(ord(i) + 32)
        else:
            r += i
    return r


def uppercase(A):
    # return [x.upper() for x in A]
    r = ""
    for i in A:
        if 97 <= ord(i) <= 122:
            r += chr(ord(i) - 32)
        else:
            r += i
    return r


def toggle_case(A):
    # return "".join([x.swapcase() for x in A])

    r = ""
    for i in A:
        r += chr(ord(i) ^ (1 << 5))
    return r

    # r = ""
    # for i in A:
    #     if 65 <= ord(i) <= 90:
    #         r += lowercase(i)
    #     elif 97 <= ord(i) <= 122:
    #         r += uppercase(i)
    #     else:
    #         r += i
    # return r


def is_alphnum(A):
    for i in A:
        if not i.isalnum():
            return 0
    return 1


def verify_immutable():
    r = ""
    for i in range(3):
        r += "a"
        print(id(r))

    print(id("a"))


if __name__ == '__main__':
    print(lowercase("LaLIT"))
    print(uppercase("lalIt"))
    print(toggle_case("Lalit Suthar"))
    verify_immutable()
