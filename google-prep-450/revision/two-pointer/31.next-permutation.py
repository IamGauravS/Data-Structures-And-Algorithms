#
# @lc app=leetcode id=31 lang=python3
#
# [31] Next Permutation
#

# @lc code=start
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        ind = -1
        for i in range(len(nums)-2, -1, -1):
            if nums[i] < nums[i+1]:
                ind = i
                break

        if ind == -1:
            nums.reverse()
            return 

   

        for j in range(len(nums)-1, ind, -1):
            if nums[j] > nums[ind]:
                nums[j], nums[ind] = nums[ind], nums[j]
                break

        nums[ind+1:]  =  reversed(nums[ind+1:])
        return 


        
# @lc code=end

