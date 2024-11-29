#
# @lc app=leetcode id=410 lang=python3
#
# [410] Split Array Largest Sum
#

# @lc code=start
class Solution:
    def getNoOfPartitions(self, nums, maxValue):
        partions = 0
        currVal = 0

        for i in range(len(nums)):
            if currVal + nums[i] > maxValue:
                partions += 1
                currVal = 0

            currVal += nums[i]
            

        return partions + 1
    
    def splitArray(self, nums: List[int], k: int) -> int:
        if len(nums) < k:
            return -1
        
        start = max(nums)
        end  = sum(nums)

        while start <= end:
            mid = (start + end) // 2

            noOfPartitions = self.getNoOfPartitions(nums, mid)

            if noOfPartitions > k:
                start = mid + 1
            else:
                end = mid - 1
                minSum = end 

        return minSum


        
# @lc code=end

