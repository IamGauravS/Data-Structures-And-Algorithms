class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        numsCircular = nums + nums

        nextGreaterArray = []
        stack = []

        for num in reversed(numsCircular):
            while len(stack) > 0 and stack[-1] <= num:
                stack.pop()

            if stack:
                nextGreaterArray.append(stack[-1])
            else:
                nextGreaterArray.append(-1)

            stack.append(num)


        nextGreaterArray = nextGreaterArray[::-1]

        return nextGreaterArray[:len(nums)]