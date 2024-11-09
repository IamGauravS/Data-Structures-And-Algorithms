#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        """
            This function returns the maximum amount a robber can rob
            without alerting the police. We use a bottoms up dp in this function
            and at every step we decide if we want to rob the current house or not.

            Args:
                nums (List[int]) : a list containg amount in each house
            Returns:
                maxAmount (int) : max amount that we can steal from all houses without getting caught
        """

        if len(nums) == 1:
            return nums[0]
        
        if len(nums) == 2:
            return max(nums[0], nums[1])
        
        ## since we would be starting the loop from 3rd house thus prevAmount would 
        ## be the max amount that we have stolen till second house and prevPrevAmount would
        ## be max amount that we have stoles till first house
        prevAmount = max(nums[0], nums[1]) 
        prevprevAmount = nums[0]

        maxAmount = 0  ## a variable to store currAmount that we have stolen till now

        for i in range(2, len(nums)):
            ## curr amount would be max of if we stole from ith and i-2th house vs i-1 house
            maxAmount = max(prevprevAmount + nums[i], prevAmount) 

            ## update prevAmount and prevprevAmount
            prevprevAmount, prevAmount = prevAmount, maxAmount

        return maxAmount
        
# @lc code=end

