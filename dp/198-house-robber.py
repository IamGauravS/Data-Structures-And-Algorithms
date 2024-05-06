class Solution:
    def rob(self, nums: List[int]) -> int:
        robbedAmount = []
        noOfHouse = len(nums)

        if noOfHouse == 1:
            return nums[0]
        
        robbedAmount.append(nums[0])
        robbedAmount.append(max(nums[0], nums[1]))

        for i in range(2, noOfHouse):
            currAmount = max(robbedAmount[i-1], robbedAmount[i-2] + nums[i])
            robbedAmount.append(currAmount)

        return robbedAmount[-1]



