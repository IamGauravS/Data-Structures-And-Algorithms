#
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#

# @lc code=start
class Solution:
    def wordBreakHelper(self, s, start):
        if start == len(s):
            return True 
        
        if start in self.memDict:
            return self.memDict[start]

        for i in range(start+1, len(s) + 1):
            if s[start:i] in self.wordDict:
                if self.wordBreakHelper(s, i):
                    self.memDict[(start)] = True 
                    return self.memDict[(start)]
                

        self.memDict[(start)] = False 
        return self.memDict[(start)]

        
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        self.memDict = {}
        self.wordDict = set(wordDict)
        self.wordDict.add("")

        return self.wordBreakHelper(s, 0)
        
# @lc code=end

