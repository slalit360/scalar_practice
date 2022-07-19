"""
Q : Missing Numbers

Array of size n contains elements in the range [1 :N+2] except two elements.
find those 2 no's
"""


# for this problem we could use following approaches:-
# 1. for loop from 1 to n+2 and check in array with O(n^2)
# 2. using freq hashmap with O(n)
# 3. sort and then count freq O(n * log n)
# 4. map elements to index, find missing idx,val pair
# 5. generate new array from 1 to N+2 and append then similar to single number three problem with O(n) & sc O(1)

# 6. (sum of no 1 to N+2) - sum of array = a + b
# (sum of squares no 1 to N) - (sum of squares of element of array) = a^2 + b^2
# we got (a^2 + b^2) and a+b now find a and b
def missing_number_4(A):
    m = len(A)
    n = m + 2
    sum_of_n = (n * (n + 1)) // 2
    sum_of_a = sum(A)
    sum_of_sqr_of_n = (n * (n+1) * (2*n+1)) // 6
    sum_of_sqr_of_a = sum([i*i for i in A])    # a^2+b^2

    a_plus_b = sum_of_n - sum_of_a  # a + b
    a2_plus_b2 = sum_of_sqr_of_n - sum_of_sqr_of_a  # a**2 + b**2

    # (a+b)^2 = a^2 + b^2 + 2ab
    ab2 = (a_plus_b ** 2) - a2_plus_b2
    # (a-b)^2 = a^2 + b^2 - 2ab
    a_minus_b = int((a2_plus_b2 - ab2) ** 0.5)




if __name__ == '__main__':
    A = [3, 6, 1, 4]
    print(missing_number_4(A))
