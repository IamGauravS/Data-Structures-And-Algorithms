#
# @lc app=leetcode id=686 lang=python3
#
# [686] Repeated String Match
#

# @lc code=start
class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        q = (len(b) - 1) // len(a) + 1
        
        for i in range(2):
            if b in a*(q+i):
                return q+i

        return -1
        
# @lc code=end

