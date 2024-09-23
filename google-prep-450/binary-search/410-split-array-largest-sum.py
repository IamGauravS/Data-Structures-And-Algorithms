import sys

class Solution:
    def canBeSplit(self, maxvalue):
        numberOfSplitsPossible = 0
        currSum = 0
        for num in self.nums:
            currSum = currSum + num 

            if currSum > maxvalue:
                numberOfSplitsPossible += 1
                currSum = num 

        if currSum <= maxvalue:
            numberOfSplitsPossible += 1

        return numberOfSplitsPossible

    def splitArray(self, nums: List[int], k: int) -> int:
        self.nums = nums

        low = max(self.nums)
        high = sum(self.nums)

        minSum = sys.maxsize

        while low <= high:
            pivot = (low+high)//2

            if self.canBeSplit(pivot) > k:
                low = pivot + 1

            else:
                high = pivot - 1
                minSum = pivot 


        return minSum 
        