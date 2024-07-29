
class Solution:
    def subsetWithDupHelper(self, nums, output, temp, index):
        if index == len(nums):
            output.append(temp[:])
            return 
        ## take the element here we can take either 1 or any number of instances of element
        temp.append(nums[index])
        self.subsetWithDupHelper(nums, output, temp, index+1)
        temp.pop()
        
        ## do not take the element when we do this we do not want to take any instance of that element
        while index+1 < len(nums) and nums[index] == nums[index+1]:
            index = index + 1
        self.subsetWithDupHelper(nums, output, temp, index+1)
        return 
        
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        output = []
        temp = []
        index =0
        nums.sort()
        self.subsetWithDupHelper(nums, output, temp, index)
        return output
        
        