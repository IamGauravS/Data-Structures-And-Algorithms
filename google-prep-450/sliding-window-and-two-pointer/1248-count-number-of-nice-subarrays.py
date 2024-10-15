class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        nums = nums % 2

        prefixSumDict = {}
        prefixSumDict[0] = 1
        currSum = 0
        count = 0

        for end in range(len(nums)):
            currSum += nums[end]

            if currSum - k in prefixSumDict:
                count += prefixSumDict[currSum - k]

            if currSum in prefixSumDict:
                prefixSumDict[currSum] += 1
            else:
                prefixSumDict[currSum] = 1


        return count 
