class Solution:
    def maxDepth(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        maxDepth = 0
        
        stack = []
        for ch in s:
            if ch not in ('(' , ')'):
                continue 
                
            if ch == '(':
                stack.append(ch)
            if ch == ')':
                maxDepth = max(len(stack), maxDepth)
                stack.pop()
        
        return maxDepth
                
            