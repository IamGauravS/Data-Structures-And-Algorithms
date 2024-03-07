def find_corrupt_pair(nums):
    i = 0
    while i < len(nums):
        if nums[i] != nums[nums[i] - 1]:  # don't get stuck in loop due to duplicate
            nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]  # swap
        else:
            i += 1

    for i, num in enumerate(nums):
        if i != num - 1:
            duplicate_num = nums[i]
            missing_num = i + 1
            return [duplicate_num, missing_num]