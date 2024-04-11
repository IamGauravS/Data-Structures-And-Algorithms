class Solution:
    def rob(self, nums: List[int]) -> int:
        noOfHouses = len(nums)
        if noOfHouses == 1:
            return nums[0]
        if noOfHouses == 2:
            return max(nums[0], nums[1])
        
        dp = [-1]*noOfHouses
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        for i in range(2, noOfHouses):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i])
            
        return dp[noOfHouses-1]
        