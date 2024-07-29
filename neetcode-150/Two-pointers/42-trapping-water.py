class Solution:
    def trap(self, height: List[int]) -> int:
        suffix_max = [0 for i in range(len(height))]
        
        
        suffix_max[len(height)-1] = len(height)-1
        
        for i in range(len(height)-2, -1, -1):
            if height[i] >= height[suffix_max[i+1]]:
                suffix_max[i] = i
            else:
                suffix_max[i] = suffix_max[i+1]
                
        prefix_max = [0 for i in range(len(height))]
        prefix_max[0] = 0
        for i in range(1, len(height)):
            if height[i] >= height[prefix_max[i-1]]:
                prefix_max[i] = i 
            else:
                prefix_max[i] = prefix_max[i-1]
                
        amount = 0
        
        for i in range(len(height)):
            if suffix_max[i] != i and prefix_max[i] != i :
                if min(height[prefix_max[i]], height[suffix_max[i]]) - height[i] > 0:
                    amount += min(height[prefix_max[i]], height[suffix_max[i]]) - height[i]
            
        return amount  
    
    
class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) -1 
        max_left = height[left]
        max_right = height[right]
        res = 0
        while left < right:
            
            if max_left < max_right:
                left +=1 
                max_left = max(max_left, height[left])
                res += max_left - height[left]
            else:
                right +=1
                max_right = max(max_right, height[right])
                res += max_right - height[right]
                
        return res
        
            