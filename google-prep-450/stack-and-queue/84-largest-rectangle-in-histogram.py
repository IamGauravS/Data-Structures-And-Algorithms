class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        nextSmallestHeight = [len(heights)]*len(heights)
        stack = []

        for i in range(len(heights) - 1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()

            if stack:
                nextSmallestHeight[i] = stack[-1]

            stack.append(i)

        prevSmallestHeight = [-1]*len(heights)
        stack = []

        for i in range(len(heights)):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()

            if stack:
                prevSmallestHeight[i] = stack[-1]

            stack.append(i)

        largestRectangle = 0

        for i in range(len(heights)):
            currHeight = heights[i] * (nextSmallestHeight[i] - prevSmallestHeight[i] - 1)
            largestRectangle = max(currHeight, largestRectangle)

        return largestRectangle