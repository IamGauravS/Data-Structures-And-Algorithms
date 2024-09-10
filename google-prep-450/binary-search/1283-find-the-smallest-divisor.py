import math
class Solution:
    def getCurrentSum(self, divisor, threshold):
        currSum = 0
        for num in self.nums:
            currSum += math.ceil(num/divisor)

        if currSum <= threshold:
            return True
        else:
            return False
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        self.nums = nums

        start = 1 
        end = max(nums)

        minDivisor = end 

        while start <= end:
            divisor = (start + end)//2

            if self.getCurrentSum(divisor, threshold):
                minDivisor = divisor 
                end = divisor - 1

            else:
                start = divisor + 1

        return minDivisor