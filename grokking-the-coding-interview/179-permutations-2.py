def print_unique_permutations(nums):
    def backtrack(start, end):
        # If at the end of the array, add the permutation to the results
        if start == end:
            result.append(nums[:])
            return
        for i in range(start, end):
            # Skip duplicate permutations
            if nums[i] != nums[start] or i == start:
                # Swap current element with the start element
                nums[start], nums[i] = nums[i], nums[start]
                # Generate permutations for the rest of the list
                backtrack(start + 1, end)
                # Undo the swap
                nums[start], nums[i] = nums[i], nums[start]

    nums.sort()
    result = []
    backtrack(0, len(nums))
    return result