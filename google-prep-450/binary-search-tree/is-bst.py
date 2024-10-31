import sys

class Solution:
    
        
    def isBSTTraversal(self, arr):
        if len(arr) <= 1:
            return True
        
        for i in range(1, len(arr)):
            if arr[i-1] >= arr[i]:
                return False
                
        return True
        