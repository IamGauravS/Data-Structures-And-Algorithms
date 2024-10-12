class Solution:
    def maxDepth(self, s: str) -> int:
        count = 0
        outputCount = 0

        for ch in s:
            if ch == '(':
                count += 1
                if count < outputCount:
                    outputCount = count 

            elif ch == ')':
                count -= 1


        return outputCount