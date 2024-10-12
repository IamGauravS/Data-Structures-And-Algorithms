class Solution:
    def largestOddNumber(self, num: str) -> str:
        start = 0
        end = len(num) - 1

        while end >= start:
            if int(num[end]) % 2 != 0:
                break
            end -= 1

        if end == -1:
            return ""
        
        return num[start:end+1]




