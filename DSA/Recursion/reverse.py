import sys

sys.setrecursionlimit(10 ** 6)


def print_rev(string):
    if len(string) == 0:
        return

    print_rev(string[1:])
    print(string[0], end='')


def inplace_rev(a, i=None, j=None):
    # if not i:
    #     i = 0
    # if not j:
    #     j = len(a) - 1
    if i >= j:
        return
    else:
        a[i], a[j] = a[j], a[i]
        return inplace_rev(a, i + 1, j - 1)


if __name__ == '__main__':
    A = "lalit"
    print_rev(A)

    print("\n")
    A = list(A)
    inplace_rev(A, 0, len(A) -1)
    print("".join(A))
