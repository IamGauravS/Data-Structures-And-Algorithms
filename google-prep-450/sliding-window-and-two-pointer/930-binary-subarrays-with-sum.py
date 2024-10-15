from collections import defaultdict

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefixSumCount = defaultdict(int)
        prefixSumCount[0] = 1  # Initialize to handle subarrays that directly match the goal
        
        currSum = 0
        noOfSubArrays = 0

        for num in nums:
            currSum += num
            
            # Check if there's a prefix sum that gives a valid subarray with sum == goal
            if currSum - goal in prefixSumCount:
                noOfSubArrays += prefixSumCount[currSum - goal]

            # Update the prefix sum count for the current sum
            prefixSumCount[currSum] += 1

        return noOfSubArrays


class Solution:
    def numSubarraysWithSumHelper(self, nums: List[int], goal: int) -> int:

        if goal < 0:
            return 0
        
        start = 0
        end = 0
        count = 0
        currSum = 0

        while end < len(nums):
            currSum += nums[end]
            while currSum > goal:
                currSum -= nums[start]
                start += 1

            count += (end - start + 1)
            end += 1

        ## count of pairs with sum goal - 1
        return count 
    
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:

        return self.numSubarraysWithSumHelper(nums, goal) - self.numSubarraysWithSumHelper(nums, goal-1)
