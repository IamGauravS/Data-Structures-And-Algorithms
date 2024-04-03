class Solution:
    def permuteHelper(self, nums, output, temp):
        if len(nums) == 0:
            output.append(temp[:])
            return 
        
        
        for i in range(len(nums)):
            
            temp.append(nums[i])
            self.permuteHelper(nums[0:i]+nums[i+1:], output, temp)
            temp.pop()
            
        return 
            
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]
        
        output = []
        
        temp = []
        self.permuteHelper(nums, output, temp)
        return output
        
        
        
## iterative approach

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        out = []
        stack = [[]] # Start with empty list

        while stack:
            curr = stack.pop()

            # Found a list with the same length as nums, add to answer
            if len(curr) == len(nums):
                out.append(curr)
                continue

            for num in nums:
                if num not in curr:
                    stack.append((curr + [num])) # Could also do append, then pop

        return out
    
    
## if numbers are not unique

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start, end):
            if start == end:
                output.append(nums[:])
            for i in range(start, end):
                if nums[i] != nums[start] or i == start:
                    nums[start], nums[i] = nums[i], nums[start]
                    backtrack(start + 1, end)
                    nums[start], nums[i] = nums[i], nums[start]

        nums.sort()
        output = []
        backtrack(0, len(nums))
        return output