#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramDict = defaultdict(list)
        for string in strs:
            key = tuple(sorted(string))
            anagramDict[key].append(string)

        return list(anagramDict.values())

        
# @lc code=end

