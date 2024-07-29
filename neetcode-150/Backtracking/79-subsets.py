class Solution:
    def subsetHelper(self, nums, index, output, temp):
        if index == len(nums):
            output.append(temp[:])
            return 
        ## take current value
        temp.append(nums[index])
        self.subsetHelper(nums, index+1, output, temp)
        ## do not take current value
        temp.pop()
        self.subsetHelper( nums, index+1, output, temp)
        return 
        
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = []
        temp = []
        self.subsetHelper(nums, 0, output, temp)
        
        return output
        