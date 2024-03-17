def permute(nums, index, output):
    if index == len(nums) - 1:
        output.append(nums[:])
        return

    for i in range(index, len(nums)):
        nums[index], nums[i] = nums[i], nums[index]
        permute(nums, index + 1, output)
        nums[index], nums[i] = nums[i], nums[index]  # backtrack

def print_all_permutation(nums):
    output = []
    permute(nums, 0, output)
    return output