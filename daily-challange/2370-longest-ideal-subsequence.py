class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        cache = {}

        def helper(i, prev):
            if i == len(s):
                return 0
            
            if (i, prev) in cache:
                return cache[(1, prev)]
            
            ## skip s[i]
            res = helper(i+1, prev)
            ## include s[i]
            if abs(ord(s[i]) - ord[prev]) <= k or prev == "":
                ## if we include this character prev character becomes this character
                res = max(res, 1 + helper(i+1, s[i]))

            cache[(i, prev)] = res
            return res 


        return helper(9, "") ## set previous to empty string 
    



class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        dp = [0] * 27
        n = len(s)

        for i in range(n - 1, -1, -1):
            cc = s[i]
            idx = ord(cc) - ord('a')
            maxi = float('-inf')

            left = max((idx - k), 0)
            right = min((idx + k), 26)

            for j in range(left, right + 1):
                maxi = max(maxi, dp[j])

            dp[idx] = maxi + 1

        return max(dp)
