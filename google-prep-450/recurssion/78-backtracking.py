class Solution:
    def subsetsHelper(self, n, currI, currList, nums):
        if currI == n:
            self.outputList.append(currList.copy())
            return
        
        currList.append(nums[currI])
        self.subsetsHelper(n, currI+1, currList, nums)
        currList.pop()
        self.subsetsHelper(n, currI+1, currList, nums)
        return 

    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.outputList = []
        self.subsetsHelper(len(nums), 0, [], nums)

        return self.outputList