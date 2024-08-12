class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        noOfSubarray = 0

        increasingSum = [0]
        currSum = 0
        for i in range(len(nums)):
            currSum +=nums[i]
            increasingSum.append(currSum)
            

        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if increasingSum[j+1] - increasingSum[i] == k:
                    noOfSubarray +=1
                

        return noOfSubarray


## more optimal

from typing import List
from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        noOfSubarray = 0
        currSum = 0
        sumFrequency = defaultdict(int)
        sumFrequency[0] = 1  # To handle the case when subarray starts from index 0

        for num in nums:
            currSum += num
            if (currSum - k) in sumFrequency:
                noOfSubarray += sumFrequency[currSum - k]
            sumFrequency[currSum] += 1

        return noOfSubarray
    
