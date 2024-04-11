class Solution:
    def isPalindrome(self, i, j):
        if self.dp[i][j] != -1:
            return self.dp[i][j]
        
        if self.s[i] != self.s[j]:
            self.dp[i][j] = 0
             
        elif j-i <=2:
            self.dp[i][j] = 1 
            
        else:
            self.dp[i][j] = self.dp[i+1][j-1]
            
        return self.dp[i][j]
        
    def longestPalindrome(self, s: str) -> str:
        self.s = s
        lenStr = len(self.s) 
        if lenStr == 1:
            return s 
        
        self.dp = [[-1 for i in range(lenStr)] for j in range(lenStr)]
        
        for i in range(lenStr):
            self.dp[i][i] = 1 
            
        longestStr = ""
        longestStrLen = 0 
        
        for i in range(lenStr-1,-1,-1):
            for j in range(i,lenStr):
                if self.dp[i][j] == -1:
                    self.isPalindrome(i,j)
                    
                if self.dp[i][j]:
                    if j-i+1 > longestStrLen:
                        longestStr = s[i:j+1]
                        longestStrLen = j-i+1
                            
        return longestStr
    
    
## more optimal solution 
## take care of even odd
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(i, j):
            left = i
            right = j
            
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
                
            return right - left - 1
        
        ans = [0, 0]

        for i in range(len(s)):
            odd_length = expand(i, i)
            if odd_length > ans[1] - ans[0] + 1:
                dist = odd_length // 2
                ans = [i - dist, i + dist]

            even_length = expand(i, i + 1)
            if even_length > ans[1] - ans[0] + 1:
                dist = (even_length // 2) - 1
                ans = [i - dist, i + 1 + dist]
                
        i, j = ans
        return s[i:j + 1]