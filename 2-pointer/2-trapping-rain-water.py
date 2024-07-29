def trapped_water(nums):
    if not nums:
        return 0

    prefix_max_array = [0]*len(nums)
    suffix_max_array = [0]*len(nums)
    water = 0

    prefix_max_array[0] = nums[0]
    for i in range(1, len(nums)):
        prefix_max_array[i] = max(prefix_max_array[i-1], nums[i])

    suffix_max_array[-1] = nums[-1]
    for i in range(len(nums)-2, -1, -1):
        suffix_max_array[i] = max(suffix_max_array[i+1], nums[i])

    for i in range(len(nums)):
        water += min(prefix_max_array[i], suffix_max_array[i]) - nums[i]

    return water


## more optimal approach using two pointer

def trapped_water(nums):
    if not nums:
        return 0

    left, right = 0, len(nums) - 1
    left_max, right_max = nums[left], nums[right]
    water = 0

    while left < right:
        if nums[left] < nums[right]:
            left += 1
            left_max = max(left_max, nums[left])
            water += left_max - nums[left]
        else:
            right -= 1
            right_max = max(right_max, nums[right])
            water += right_max - nums[right]

    return water