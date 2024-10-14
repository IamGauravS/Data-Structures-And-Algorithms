class Solution:
    def combinationSumHelper(self, currIdx, currSum, currArr):
        if len(currArr) == self.arrLen:
            if currSum == self.target:
                self.output.append(currArr[:])
            return 
        
        if currSum >= self.target or currIdx >= 9:
            return 
        
        currArr.append(self.nums[currIdx])
        self.combinationSumHelper(currIdx+1, currSum + self.nums[currIdx], currArr)

        currArr.pop()
        self.combinationSumHelper(currIdx+1, currSum, currArr)
        return
        
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.nums = [1,2,3,4,5,6,7,8,9]
        self.output = []
        self.target = n
        self.arrLen = k 

        self.combinationSumHelper(0, 0, [])

        return self.output
    

## slightly optimsied version

from typing import List

class Solution:
    def combinationSumHelper(self, nums, target, arrLen, currIdx, currSum, currArr, output):
        if len(currArr) == arrLen:
            if currSum == target:
                output.append(currArr[:])
            return 
        
        if currSum >= target or currIdx >= len(nums):
            return 
        
        # Include the current number and recurse
        currArr.append(nums[currIdx])
        self.combinationSumHelper(nums, target, arrLen, currIdx + 1, currSum + nums[currIdx], currArr, output)

        # Exclude the current number and recurse
        currArr.pop()
        self.combinationSumHelper(nums, target, arrLen, currIdx + 1, currSum, currArr, output)
        
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        output = []
        self.combinationSumHelper(nums, n, k, 0, 0, [], output)
        return output