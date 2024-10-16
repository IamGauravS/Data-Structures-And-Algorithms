from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tCountDict = defaultdict(int)
        for ch in t:
            tCountDict[ch] += 1

        required = len(tCountDict)
        formed = 0
        minLen = float('inf')
        minStr = ""
        start = 0
        sCountDict = defaultdict(int)

        for end in range(len(s)):
            if s[end] in tCountDict:
                sCountDict[s[end]] += 1
                if sCountDict[s[end]] == tCountDict[s[end]]:
                    formed += 1

            while formed == required:
                currLen = end - start + 1
                if currLen < minLen:
                    minStr = s[start:end+1]
                    minLen = currLen
                if s[start] in tCountDict:
                    sCountDict[s[start]] -= 1
                    if sCountDict[s[start]] < tCountDict[s[start]]:
                        formed -= 1

                start += 1

        return minStr if minLen != float('inf') else ""