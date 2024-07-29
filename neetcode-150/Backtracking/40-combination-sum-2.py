class Solution:
    def combinationSumHelper(self, candidates, output, subSet, currIndex, currSum, target):
        if currIndex == len(candidates):
            if currSum == target:
                output.append(subSet[:])
            return 
        
        ## we take the current instance of that element and any other instance
        if currSum + candidates[currIndex] <= target:
            subSet.append(candidates[currIndex])
            self.combinationSumHelper(candidates, output, subSet, currIndex+1, currSum + candidates[currIndex], target)
            subSet.pop()
            
        ## we do not take any instance of that element
        while currIndex+1 < len(candidates) and candidates[currIndex] == candidates[currIndex+1]:
            currIndex +=1 
        self.combinationSumHelper(candidates, output, subSet, currIndex+1, currSum, target)
        
        return 
        
    
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        currSum = 0
        output = []
        currIndex = 0
        candidates.sort()
        
        self.combinationSumHelper(candidates, output, [], currIndex, currSum, target)
        
        return output
        