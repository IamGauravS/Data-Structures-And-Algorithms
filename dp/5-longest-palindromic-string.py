class Solution:
    def longestPalindrome(self, s: str) -> str:
        lenStr = len(s)

        if lenStr == 0:
            return 0
        dp = [[0]*lenStr for i in range(lenStr)]

        maxPalindromelen = 1 
        maxPalindromeStr = s[0]
        

        for i in range(lenStr-1, -1, -1):
            for j in range(i, lenStr, 1):
                if s[i] == s[j]:
                    if j-i <=2:
                        dp[i][j] = j-i+1

                    else:
                        if dp[i+1][j-1] >0:
                            dp[i][j] = dp[i+1][j-1] + 2

                if dp[i][j] > maxPalindromelen:
                    maxPalindromelen = dp[i][j]
                    maxPalindromeStr = s[i:j+1]


        return maxPalindromeStr
