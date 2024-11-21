#
# @lc app=leetcode id=28 lang=python3
#
# [28] Find the Index of the First Occurrence in a String
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack):
            return -1

        lenNeedle = len(needle)
        lenHaystack = len(haystack)

        for i in range(lenHaystack-lenNeedle+1):
            if haystack[i:i+lenNeedle] == needle:
                return i 


        return -1
        
# @lc code=end

