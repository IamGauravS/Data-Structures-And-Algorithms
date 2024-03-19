class Solution:
    def rob_helper(self, nums_input):
        
        if len(nums_input) == 1:
            return nums_input[0]
        
        dp = []
        dp.append(0)
        dp.append(nums_input[0])
        
        for i in range(2, len(nums_input)+1):
            dp.append(max(dp[i-1], dp[i-2]+nums_input[i-1]))
            
        return dp[-1]
    
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 0:
            return 0
        
        if len(nums) == 1:
            return nums[0]
        
        if len(nums) == 2:
            return max(nums[0], nums[1])

        robbed_amount_with_first_house = self.rob_helper(nums[:-1])
        robbed_amount_with_last_house = self.rob_helper(nums[1:])
        
        return max(robbed_amount_with_first_house, robbed_amount_with_last_house)