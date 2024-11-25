#
# @lc app=leetcode id=91 lang=python3
#
# [91] Decode Ways
#

# @lc code=start
class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == 0:
            return 0
        
        noOfWays = [0]*len(s)
        noOfWays[0] = 1

        for i in range(1, len(s)):
            if s[i] == 0:
                if s[i-1] in ("1", "2"):
                    noOfWays[i] = noOfWays[i-1]
                else:
                    return 0

            else:
                if i > 1:
                    if int(s[i-1:i+1]) < 26:
                        noOfWays[i] = noOfWays[i-1] + noOfWays[i-2]

                    else:
                        noOfWays[i] = noOfWays[i-1]
                else:
                    if int(s[i-1:i+1]) <= 26:
                        noOfWays[i] = noOfWays[i-1] + 1

                    else:
                        noOfWays[i] = noOfWays[i-1]


        return noOfWays[-1]
                
        
# @lc code=end
