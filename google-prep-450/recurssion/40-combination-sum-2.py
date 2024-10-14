class Solution:
    def combinationSumHelper(self, currI, currSum, currArr):
        if currSum == self.target:
            self.uniqueCombinations.append(currArr.copy())
            return 
        if currSum > self.target or currI >= self.candidatesLen:
            return 
       
        
        ## here if we pick we allow all possibilities of future elements to be picked
        currArr.append(self.candidates[currI])
        self.combinationSumHelper(currI+1, currSum + self.candidates[currI], currArr)
        

        ## if we don't pick we don't pick any instance of that element
        while currI < self.candidatesLen-1 and self.candidates[currI] == self.candidates[currI+1]:
            currI += 1

        currArr.pop()
        self.combinationSumHelper(currI+1, currSum , currArr)
        return        

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.uniqueCombinations = []
        candidates.sort()
        self.candidates = candidates.copy()
        self.target = target 
        self.candidatesLen = len(candidates)

        self.combinationSumHelper(0,0,[])

        return self.uniqueCombinations