
def longestConsecutive(nums) -> int:
    longest_streak = 0
    num_set = set(nums)

    for num in num_set:
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1
            while current_num + 1 in num_set:
                print(current_num, end="\t")
                current_num += 1
                current_streak += 1
            print(current_num, end="\t")
            longest_streak = max(longest_streak, current_streak)
            print(" ")

    return longest_streak


if __name__ == '__main__':
    print("length : ", longestConsecutive([1, 6, 3, 7, 2, 9, 0, 4]))