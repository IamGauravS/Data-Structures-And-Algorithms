#
# @lc app=leetcode id=921 lang=python3
#
# [921] Minimum Add to Make Parentheses Valid
#

# @lc code=start
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        if not s:
            return 0
        
        minMoves = 0

        stack = []
        for ch in s:
            if ch == '(':
                stack.append(ch)
            else:
                if len(stack) == 0:
                    minMoves += 1
                elif stack[-1] == '(':
                    stack.pop()

        return minMoves + len(stack)
        
# @lc code=end

