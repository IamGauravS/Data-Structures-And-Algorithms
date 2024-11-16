#
# @lc app=leetcode id=1048 lang=python3
#
# [1048] Longest String Chain
#

# @lc code=start
from typing import List

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        # Sort words by their lengths
        words.sort(key=len)
        
        # Dictionary to store the longest chain length for each word
        dp = {}
        max_length = 0

        for word in words:
            dp[word] = 1  # Each word is a chain of at least length 1
            # Try removing each character from the word to form a predecessor
            for i in range(len(word)):
                predecessor = word[:i] + word[i+1:]
                if predecessor in dp:
                    dp[word] = max(dp[word], dp[predecessor] + 1)
            # Update the maximum chain length
            max_length = max(max_length, dp[word])

        return max_length

# Example usage:
        
# @lc code=end

