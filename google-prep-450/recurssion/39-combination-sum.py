class Solution:
    def combinationSumHelper(self, currI, currSum, currArr):
        if currSum == self.target:
            self.uniqueCombinations.append(currArr.copy())
            return 
        if currSum > self.target:
            return 
        if currI >= self.candidatesLen:
            return 
        
        
        currArr.append(self.candidates[currI])
        self.combinationSumHelper(currI, currSum + self.candidates[currI], currArr)

        currArr.pop()
        self.combinationSumHelper(currI+1, currSum, currArr)

        return 

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.uniqueCombinations = []
        candidates.sort()
        self.candidates = candidates.copy()
        self.target = target 
        self.candidatesLen = len(candidates)

        self.combinationSumHelper(0,0,[])

        return self.uniqueCombinations