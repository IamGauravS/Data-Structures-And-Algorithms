class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        start = 0

        sign = 1
        if s[0] == "-" or s[0] == '+':
            if s[0] == "-":
                sign = 0
            start += 1
        
        while s[start] == '0' and start < len(s):
            start += 1

        s = s[start:]

        start = 0
        while s[start].isdigit() and start < len(s):
            start += 1

        s = s[:start]

        if len(s) == 0:
            return 0
        else:
            if sign == 0:
                return -1*int(s)
            return int(s)

        