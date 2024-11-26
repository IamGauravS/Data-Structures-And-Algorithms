#
# @lc app=leetcode id=678 lang=python3
#
# [678] Valid Parenthesis String
#

# @lc code=start
class Solution:
    def checkValidString(self, s: str) -> bool:
        stack = []
        minOpenBrackets = 0
        maxOpenBrackets = 0

        for ch in s:
            if ch == '(':
                minOpenBrackets += 1
                maxOpenBrackets += 1
            if ch == ')':
                maxOpenBrackets -= 1
                if minOpenBrackets > 0:
                    minOpenBrackets -= 1

            if ch == '*':
                maxOpenBrackets += 1
                if minOpenBrackets > 0:
                    minOpenBrackets -= 1

            if maxOpenBrackets <0:
                return False 

        return minOpenBrackets == 0

      

        
# @lc code=end

