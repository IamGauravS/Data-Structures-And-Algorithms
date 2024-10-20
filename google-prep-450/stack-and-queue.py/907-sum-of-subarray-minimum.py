class Solution:
    def nextSmallerElement(self, arr):
        n = len(arr)
        nextSmallerElementArray = [n]*n
        stack = []

        for i in range(n-1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            if stack:
                nextSmallerElementArray[i] = stack[-1]
            

            stack.append(i)

        return nextSmallerElementArray
    
    def prevSmallerElement(self, arr):
        prevSmallerElementArr = [-1]*len(arr)
        stack = []

        for i in range(len(arr)):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            if stack:
                prevSmallerElementArr.append(stack[-1])

            stack.append(i)

        return prevSmallerElementArr

    def sumSubarrayMins(self, arr: List[int]) -> int:
        
        prevSmallerElementArr = self.prevSmallerElement(arr)
        nextSmallerElementArr = self.nextSmallerElement(arr)

        totalSum = 0
        mod = 10**9 + 7
        for i in range(len(arr)):
            left = i - prevSmallerElementArr[i] 
            right = nextSmallerElementArr[i] - i 
            totalSum = (totalSum + arr[i] * left * right) % mod


        return totalSum      
    

## optimised version


class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10 ** 9 + 7
        stack = []
        sum_of_minimums = 0;

        for i in range(len(arr) + 1):
            
            # when i reaches the array length, it is an indication that
            # all the elements have been processed, and the remaining
            # elements in the stack should now be popped out.

            while stack and (i == len(arr) or arr[stack[-1]] >= arr[i]):

                # Notice the sign ">=", This ensures that no contribution
                # is counted twice. right_boundary takes equal or smaller 
                # elements into account while left_boundary takes only the
                # strictly smaller elements into account

                mid = stack.pop()
                left_boundary = -1 if not stack else stack[-1]
                right_boundary = i

                # count of subarrays where mid is the minimum element
                count = (mid - left_boundary) * (right_boundary - mid)
                sum_of_minimums += (count * arr[mid])

            stack.append(i)
        
        return sum_of_minimums % MOD
