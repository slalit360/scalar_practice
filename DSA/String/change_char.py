"""
You are given a string A of size N consisting of lowercase alphabets.

You can change at most B characters in the given string to any other lowercase alphabet such that the number
of distinct characters in the string is minimized.

Find the minimum number of distinct characters in the resulting string.
"""


def change_char(A, B):
    # TC : O(n log n) : dict + sort
    # DC : O(n)
    char_freq = dict()
    unique_char = 0
    for i in A:
        if i in char_freq:
            char_freq[i] += 1
        else:
            char_freq[i] = 1
            unique_char += 1

    for _, freq in sorted(char_freq.items(), key=lambda item: item[1]):
        if freq <= B:
            B -= freq
            unique_char -= 1

        if B == 0:
            break

    return unique_char


if __name__ == '__main__':
    print(change_char("abcdabcd", 2))
