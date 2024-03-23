import sys
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        app_set = set(nums)
        
        max_len = 0
        
        for num in nums:
            if num-1 not in app_set:
                curr_len = 1
                
                while num+1 in app_set:
                    curr_len +=1 
                    num = num+1
                    
                if curr_len > max_len:
                    max_len = curr_len 
                    
        return max_len
        
        