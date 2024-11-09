class Solution:
    def minimizeCost(self, k, arr):
        # code here
        if len(arr) == 1:
            return 0
        if k == 0:
            return -1
            
        costArray = [0, abs(arr[1]-arr[0])]
        
        for i in range(2, len(arr)):
            currMinJump = float('inf')
            for j in range(i-1, i-k-1, -1):
                if j == -1:
                    break
                currMinJump = min(costArray[j] + abs(arr[i] - arr[j]), currMinJump)
                
            costArray.append(currMinJump)
            
            
        return costArray[-1]