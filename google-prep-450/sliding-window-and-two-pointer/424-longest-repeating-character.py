class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) <= k:
            return len(s)
        
        start = 0
        lenLongestSub = 0
        countDict = {}

        for end in range(len(s)):
            if s[end] not in countDict:
                countDict[s[end]] = 0
            countDict[s[end]] += 1

            highestFreq = max(countDict.values())
            totalNumberOfChanges = (end - start + 1) - highestFreq

            while totalNumberOfChanges > k:
                countDict[s[start]] -= 1
                start += 1
                highestFreq = max(countDict.values())
                totalNumberOfChanges = (end - start + 1) - highestFreq

            lenLongestSub = max(lenLongestSub, end - start + 1)

            
        return lenLongestSub

            
## optimal

## here we dont need a while loop since we will do this as soon as it breaches the condition
## we also dont need to calculate totalNumberOfChanges again 
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) <= k:
            return len(s)
        
        start = 0
        lenLongestSub = 0
        countDict = {}
        highestFreq = 0

        for end in range(len(s)):
            if s[end] not in countDict:
                countDict[s[end]] = 0
            countDict[s[end]] += 1

            highestFreq = max(highestFreq, countDict[s[end]])
            totalNumberOfChanges = (end - start + 1) - highestFreq

            if totalNumberOfChanges > k:
                countDict[s[start]] -= 1
                start += 1

            lenLongestSub = max(lenLongestSub, end - start + 1)

        return lenLongestSub

