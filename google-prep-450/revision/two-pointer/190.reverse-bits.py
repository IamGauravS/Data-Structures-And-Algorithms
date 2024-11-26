#
# @lc app=leetcode id=190 lang=python3
#
# [190] Reverse Bits
#

# @lc code=start
class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0

        for _ in range(32):
            result = (result << 1) | (n&1)
            n >>= 1

        return result 
        
# @lc code=end

