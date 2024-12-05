#
# @lc app=leetcode id=132 lang=python3
#
# [132] Palindrome Partitioning II
#

# @lc code=start
class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0

        # Step 1: Precompute palindrome table
        is_palindrome = [[False] * n for _ in range(n)]
        for end in range(n):
            for start in range(end + 1):
                if s[start] == s[end] and (end - start <= 2 or is_palindrome[start + 1][end - 1]):
                    is_palindrome[start][end] = True

        # Step 2: DP to find the minimum cuts
        dp = [float('inf')] * n
        for i in range(n):
            if is_palindrome[0][i]:  # If s[0:i+1] is a palindrome, no cuts needed
                dp[i] = 0
            else:
                for j in range(i):
                    if is_palindrome[j + 1][i]:  # If s[j+1:i+1] is a palindrome
                        dp[i] = min(dp[i], dp[j] + 1)

        return dp[-1]

        
# @lc code=end

