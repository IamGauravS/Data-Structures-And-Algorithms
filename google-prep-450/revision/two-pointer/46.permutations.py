#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#

# @lc code=start
class Solution:
    def permuteHelper(self, nums, start, output):
        # Base case: If the current index reaches the end, add the permutation to output
        if start == len(nums):
            output.append(nums[:])  # Use a copy of the current state of nums
            return

        for i in range(start, len(nums)):
            # Swap current index with the loop index
            nums[start], nums[i] = nums[i], nums[start]
            
            # Recur for the next index
            self.permuteHelper(nums, start + 1, output)
            
            # Backtrack to restore the original state
            nums[start], nums[i] = nums[i], nums[start]

    def permute(self, nums: List[int]) -> List[List[int]]:
        output = []
        self.permuteHelper(nums, 0, output)
        return output

        
# @lc code=end

