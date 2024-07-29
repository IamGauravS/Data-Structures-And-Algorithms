class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output_dict = {}
        for i, num in enumerate(nums):
            
            element_to_find = target - num 
            if element_to_find in output_dict:
                return [i, output_dict[element_to_find]]    
            
            output_dict[num] = i 
        