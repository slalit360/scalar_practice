def get_special_index_count(A):
    # generate PSE and PSO

    n = len(A)
    PSO = [0] * n
    PSE = [0] * n

    PSE[0] = A[0]
    PSO[0] = 0
    for i in range(1, n):
        if i % 2 == 0:
            PSE[i] = PSE[i - 1] + A[i]
            PSO[i] = PSO[i - 1]
        else:
            PSE[i] = PSE[i - 1]
            PSO[i] = PSO[i - 1] + A[i]

    # PSO[0] = 0
    # for i in range(1, n):
    #     if i % 2 == 1:
    #         PSO[i] = PSO[i - 1] + A[i]
    #     else:
    #         PSO[i] = PSO[i - 1]

    count_indices = 0
    for i in range(0, n):
        even_sum = PSE[i - 1] + (PSO[n - 1] - PSO[i])
        odd_sum = PSO[i - 1] + (PSE[n - 1] - PSE[i])

        if even_sum == odd_sum:
            count_indices += 1

    return count_indices


print(get_special_index_count([2, 1, 6, 4]))

print(get_special_index_count([1, 1, 1]))

print(get_special_index_count([0,0,0,0,0,0,0,0,0,0,0,0]))
