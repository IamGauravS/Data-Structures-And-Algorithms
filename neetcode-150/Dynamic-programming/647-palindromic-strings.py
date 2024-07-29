class Solution:
    def countSubstrings(self, s: str) -> int:
        if len(s) == 1:
            return 1 
        
        lenStr = len(s)
        dp = [[0 for i in range(lenStr)] for j in range(lenStr)]
        
        palindromeCount = 0
        
        for i in range(lenStr-1, -1, -1):
            for j in range(i, lenStr):
                
                if s[i] == s[j]:
                    if j-i < 2:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = dp[i+1][j-1]
                    
                            
                if dp[i][j]:
                    palindromeCount += 1 
                    
        return palindromeCount
    
    
## optimised approach
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0
        
        # Check all substrings that have odd length
        for center in range(n):
            left = right = center
            while left >= 0 and right < n and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
                
        # Check all substrings that have even length
        for center in range(n - 1):
            left, right = center, center + 1
            while left >= 0 and right < n and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
                
        return count