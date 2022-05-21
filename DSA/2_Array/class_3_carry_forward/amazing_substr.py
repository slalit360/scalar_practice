def get_amazing_substrings_count(A):
    n = len(A)
    vowel = {'I', 'O', 'U', 'A', 'E', 'a', 'e', 'o', 'i', 'u'}
    # print(vowel)
    count = 0
    for i in range(n):
        if A[i] in vowel:
            count += n - i
    return count % 10003


if __name__ == '__main__':
    A = "ABEC"
    print(get_amazing_substrings_count(A))
