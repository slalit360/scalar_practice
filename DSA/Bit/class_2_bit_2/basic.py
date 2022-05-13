# def get_binary(N):
#     while N > 0:
#

def power_base_2(n):
    return 1 << n


def check_bit_set(n, i):
    """
    Given N and i check if ith bit of N is set or not
    """
    if n & (1 << i) == 0:
        return False
    else:
        return True


def set_bit(n, i):
    return n | (1 << i)


def unset_bit(n, i):
    return n & ~(1 << i)


def toggle_bit(n, i):
    return n ^ (1 << i)


def toggle_rightmost_bits(n, i):
    """
    given n and i, toggle all bit i msb bits
    """
    return n - 1


def set_x_unset_y(x, y):
    return ((1 << x) - 1) << y


if __name__ == '__main__':
    print(bin(set_x_unset_y(4, 3)))
