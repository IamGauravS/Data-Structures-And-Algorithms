#
# @lc app=leetcode id=424 lang=python3
#
# [424] Longest Repeating Character Replacement
#

# @lc code=start
from collections import defaultdict
class Solution:
    
    def characterReplacement(self, s: str, k: int) -> int:

        freqDict = [0]*26
        start = 0
        maxFreq = 0
        maxSubstrLen = 0

        for end in range(len(s)):
            currChar = s[end]
            freqDict[ord(currChar) - ord('A')] += 1
            maxFreq = max(maxFreq, freqDict[ord(currChar) - ord('A')])

            if (end - start + 1) - maxFreq > k:
                freqDict[ord(s[start]) - ord('A')] -= 1
                start += 1

            maxSubstrLen = max(maxSubstrLen, end-start+1)


        return maxSubstrLen
        
# @lc code=end
