
def is_even_sub_array_possible(A):
    n = len(A)
    if n % 2 != 0 or A[0] % 2 != 0 or A[n-1] % 2 != 0:
        return "NO"
    else:
        return "YES"


if __name__ == '__main__':
    A = [2, 4, 8, 6]
    A1 = [2, 4, 8, 7, 6]
    print(is_even_sub_array_possible(A))
    print(is_even_sub_array_possible(A1))