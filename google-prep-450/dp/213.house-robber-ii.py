#
# @lc app=leetcode id=213 lang=python3
#
# [213] House Robber II
#

# @lc code=start
class Solution:
    def robInAStraightLine(self, nums: List[int]) -> int:
        """
            This function returns the maximum amount a robber can rob
            without alerting the police. We use dynamin programmng and populate the
            table in bottoms up approach in this function
            and at every step we decide if we want to rob the current house or not.

            Args:
                nums (List[int]) : a list containg amount in each house
            Returns:
                maxAmount (int) : max amount that we can steal from all houses without getting caught
        """

        ## since we always will steal from first house
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        
        
        ## since we would be starting the loop from 3rd house thus maxAtPreviousHouse would 
        ## be the max amount that we have stolen till second house and maxAtTwoHousesBack would
        ## be max amount that we have stoles till first house
        maxAtPreviousHouse = max(nums[0], nums[1])  
        maxAtTwoHousesBack = nums[0]

        maxAmount = 0  ## a variable to store currAmount that we have stolen till now

        for i in range(2, len(nums)):
            ## curr amount would be max of if we stole from ith and i-2th house vs i-1 house
            maxAmount = max(maxAtTwoHousesBack + nums[i], maxAtPreviousHouse) 

            ## update maxAtPreviousHouse and maxAtTwoHousesBack
            maxAtTwoHousesBack, maxAtPreviousHouse = maxAtPreviousHouse, maxAmount

        return maxAmount
    def rob(self, nums: List[int]) -> int:
        """
            This function returns the maximum amount a robber can rob
            without alerting the police. We use dynamin programmng and populate the
            table in bottoms up approach in this function. Since the houses are arranged 
            in circular order if we decide to steal from the first house then we cannot steal 
            from last house and if we decide to steal from second house then only we can steal
            from last house
        """

        ## if there are no houses to steal from
        if len(nums) == 0:
            return 0
        
        ## if there is only one house then we have no choice other than to steal from that house
        if len(nums) == 1:
            return nums[0]
        
        ## we can return max of rob from first house and not from last or rob from second and we can rob from last
        return max(self.robInAStraightLine(nums[:-1]), self.robInAStraightLine(nums[1:]))
        
        
        
# @lc code=end

