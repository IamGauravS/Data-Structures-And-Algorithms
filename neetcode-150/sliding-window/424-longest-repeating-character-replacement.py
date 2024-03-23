class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        count = {}
        res = 0
        l = 0
        
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            ## r-l+1 is the size of window
            while (r-l+1) - max(count.values()) > k:
                count[s[l]] -= 1
                l +=1
            
            res = max(res, r-l+1)
            
            
        return res 
    
    
    
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        count = {}
        res = 0
        l = 0
        maxf = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])
            ## r-l+1 is the size of window
            while (r-l+1) - maxf > k:
                count[s[l]] -= 1
                l +=1
            
            res = max(res, r-l+1)
            
            
        return res 
            
        
            
        