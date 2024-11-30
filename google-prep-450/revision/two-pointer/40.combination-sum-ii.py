#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#

# @lc code=start
class Solution:
    def backtrack(self, candidates, currInd, currPath, target, output):
        if target == 0:
            output.append(currPath[:])
            return 
        if currInd >= len(candidates):
            return 
        

        ## take current element
        if candidates[currInd] <= target:
            self.backtrack(candidates, currInd+1, currPath+[candidates[currInd]], target-candidates[currInd], output)

        ## not take
        while currInd < len(candidates) -1 and candidates[currInd] == candidates[currInd+1]:
                currInd += 1

        self.backtrack(candidates, currInd+1, currPath, target, output)
    
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if sum(candidates) < target:
            return []
        
        candidates.sort()

        output = []
        self.backtrack(candidates, 0, [], target, output)
        return output

        
# @lc code=end

