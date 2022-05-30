"""
Q2. Check Palindrome - II

Given a string A consisting of lowercase characters.
Check if characters of the given string can be rearranged to form a palindrome.
Return 1 if it is possible to rearrange the characters of the string A such that it becomes a palindrome else return 0.

Input 1:
 A = "abcde"
Input 2:
 A = "abbaee"

Example Output
Output 1:
 0
Output 2:
 1
"""


def check_palindrome_possible(A):
    # TC : O(n)
    # SC : O(n)
    hashmap = dict()

    for i in A:
        if i not in hashmap:
            hashmap[i] = 1
        else:
            hashmap[i] += 1

    flag_cnt = 0
    for k, v in hashmap.items():
        if v & 1 == 0:  # even condition
            pass
        else:
            flag_cnt += 1

    if flag_cnt <= 1:
        return 1
    else:
        return 0


if __name__ == '__main__':
    print(check_palindrome_possible("abade"))
    print(check_palindrome_possible("abbaee"))
    print(check_palindrome_possible("abbaeek"))