#
# @lc app=leetcode id=907 lang=python3
#
# [907] Sum of Subarray Minimums
#

# @lc code=start
class Solution:
    def getNSE(self, arr):
        output = [0]*len(arr)
        stack = []

        for i in range(len(arr)-1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            if not stack:
                output[i] = len(arr)
            else:
                output[i] = stack[-1]

            stack.append(i)

        return output 


    def getPSE(self, arr):
        output = [0]*len(arr)
        stack = []

        for i in range(len(arr)):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            if not stack:
                output[i] = -1
            else:
                output[i] = stack[-1]

            stack.append(i)

        return output

    def sumSubarrayMins(self, arr: List[int]) -> int:
        nextSmallerElement = self.getNSE(arr)
        prevSmallerorEqualElement = self.getPSE(arr)

        MOD = 10**9 + 7

        total = 0

        for i in range(len(arr)):
            total += (nextSmallerElement[i] - i)*(i-prevSmallerorEqualElement[i])*arr[i]


        return total % MOD
        
# @lc code=end

