#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:
    def expandAroundCenter(self,s, left,right):
        while left >= 0 and right < len(s) and (s[left] == s[right]):
            left -= 1
            right += 1

        return (left+1, right-1)

    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s

        start, end = 0, 0
        for i in range(len(s)):

            ## odd length palindrome
            left1, right1 = self.expandAroundCenter(s, i, i)
            left2, right2 = self.expandAroundCenter(s, i, i+1)

            if right1 - left1 > end - start:
                start, end = left1, right1
            if right2 - left2 > end - start:
                start, end = left2, right2


        return s[start:end+1]



        
        
# @lc code=end

