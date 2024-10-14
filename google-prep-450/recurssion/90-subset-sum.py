class Solution:
    def subsetSumHelper(self, currIdx, currArr):
        if currIdx == self.numsLen:
            self.output.append(currArr[:])
            return

        currArr.append(self.nums[currIdx])
        self.subsetSumHelper(currIdx+1, currArr)

        while currIdx < self.numsLen - 1 and self.nums[currIdx] == self.nums[currIdx+1]:
            currIdx += 1

        currArr.pop()
        self.subsetSumHelper(currIdx+1, currArr)
        return 

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.output = []
        nums.sort()
        self.nums = nums
        self.numsLen = len(nums)
        self.subsetSumHelper(0, [])

        return self.output