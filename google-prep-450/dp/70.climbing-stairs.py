#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        """
            This function returns the number of ways we can reach a stair of height 2
            from bottom. 

            Args:
                n (int) : total number of stairs
            Returns:
                noOfWays (int) : total number of ways to reach top
        """

        ## edge case for n < 2
        if n <= 2:
            return n 
        
        prevNumOfWay = 2  ## since we will loop from 3rd step we are initialising this to 2
        prevprevNumOfWay = 1  ## to reach step 1 there is only way

        noOfWays = 0
        for i in range(3, n+1):
            ## no of ways to reach nth step = no of ways for n-1 + no of ways for n-1
            noOfWays = prevNumOfWay + prevprevNumOfWay
            prevprevNumOfWay, prevNumOfWay = prevNumOfWay, noOfWays

        return noOfWays

        
# @lc code=end

