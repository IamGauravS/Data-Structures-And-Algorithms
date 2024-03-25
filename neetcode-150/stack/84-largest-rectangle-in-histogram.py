class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        suffix_smaller = [0 for i in range(len(heights))]
        prefix_smaller = [0 for i in range(len(heights))]
        n = len(heights)
        stack = []
        
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            suffix_smaller[i] = stack[-1] if stack else -1
            stack.append(i)
            
        stack = []
        
        for i in range(n-1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            prefix_smaller[i] = stack[-1] if stack else n
            stack.append(i)
            
        
        max_area = 0
        for i in range(n):
            max_area = max(max_area, heights[i] * (prefix_smaller[i] - suffix_smaller[i] - 1))

        return max_area
                
                
## space optimised

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        suffix_smaller = [0 for i in range(len(heights))]
        
        n = len(heights)
        stack = []
        
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            suffix_smaller[i] = stack[-1] if stack else -1
            stack.append(i)
            
        stack = []
        max_area = 0
        for i in range(n-1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            prefix_smaller = stack[-1] if stack else n
            max_area = max(max_area, heights[i] * (prefix_smaller - suffix_smaller[i] - 1))
            stack.append(i)
            
        
        return max_area
                
                
