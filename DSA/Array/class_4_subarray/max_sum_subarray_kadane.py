def maxSubArray(nums) -> int:
    # kadane's algorithm
    # TC : O(N)
    # SC : O(1)
    max_sum = nums[0]
    current_sum = 0
    for i in nums:
        current_sum += i
        max_sum = max(max_sum, current_sum)
        if current_sum < 0:
            current_sum = 0
    return max_sum


if __name__ == '__main__':
    print(maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # 6
    print(maxSubArray([8, -19, 5, -4, 20]))  # 21
    print(maxSubArray([5, 4, -1, 7, 8]))  # 23
    print(maxSubArray([-2, 1]))  # 1
    print(maxSubArray([1]))  # 1
