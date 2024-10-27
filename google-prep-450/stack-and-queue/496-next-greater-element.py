class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        nextGreaterMap = {}
        stack = []

        for num in reversed(nums2):
            while stack and stack[-1] <= num:
                stack.pop()

            if stack:
                nextGreaterMap[num] = stack[-1]
            else:
                nextGreaterMap[num] = -1

            stack.append(num)


        for i in range(len(nums1)):
            ans.append(nextGreaterMap[nums1[i]])

        return ans
