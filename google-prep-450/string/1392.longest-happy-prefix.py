#
# @lc app=leetcode id=1392 lang=python3
#
# [1392] Longest Happy Prefix
#

# @lc code=start
class Solution:
    def longestPrefix(self, s: str) -> str:

        MOD = 10**9 + 7
        base = 29

        n = len(s)
        prefix_hash = 0
        suffix_hash = 0
        base_power = 1
        longest_prefix_length = 0

        for i in range(n - 1):
            prefix_hash = (prefix_hash * base + (ord(s[i]) - ord('a'))) % MOD
            suffix_hash = (suffix_hash + (ord(s[n - 1 - i]) - ord('a')) * base_power) % MOD
            base_power = (base_power * base) % MOD

            if prefix_hash == suffix_hash:
                longest_prefix_length = i + 1

        return s[:longest_prefix_length]



        
# @lc code=end

