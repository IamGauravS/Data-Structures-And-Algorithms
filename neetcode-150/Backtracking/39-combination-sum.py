class Solution:
    def combinationSumHelper(self, candidates, index, output, temp, curr_sum, target):
        if index == len(candidates):
            if curr_sum == target:
                output.append(temp[:])
            return
                
        ## take condition
        if curr_sum + candidates[index] <= target:
            temp.append(candidates[index])
            self.combinationSumHelper(candidates, index, output, temp, curr_sum+candidates[index], target)
            temp.pop()
        ## not take
        self.combinationSumHelper(candidates, index+1, output, temp, curr_sum, target)
        
        return 
                
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        output = []
        temp = []
        curr_sum = 0
        self.combinationSumHelper(candidates, 0, output, temp, curr_sum, target)
        return output