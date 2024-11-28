#
# @lc app=leetcode id=516 lang=python3
#
# [516] Longest Palindromic Subsequence
#

# @lc code=start
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]

        # Single character is a palindrome of length 1
        for i in range(n):
            dp[i][i] = 1

        # Fill DP table for substrings of increasing lengths
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1  # End index of the substring
                if s[i] == s[j]:
                    dp[i][j] = 2 + dp[i + 1][j - 1]
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        return dp[0][n - 1]  # Longest palindromic subsequence for the entire string


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        one_index = 0
        two_index = len(nums)-1
        index = 0

        while one_index < two_index:
            if nums[index] == 0:
                index += 1
            
            else:
                if nums[one_index] < nums[two_index]:  
                    nums[one_index], nums[two_index] == nums[two_index], nums[one_index]  
                    one_index += 1
                    index += 1
                else:
                    nums[one_index], nums[two_index] == nums[two_index], nums[one_index]
                    two_index
                    two_index -= 1
                    index += 1

        return nums
# @lc code=end

