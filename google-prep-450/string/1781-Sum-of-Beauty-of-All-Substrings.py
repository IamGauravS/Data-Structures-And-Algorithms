from collections import defaultdict
class Solution:
    def getFreq(self, hashMap):
        values = hashMap.values()
        return min(values), max(values)
    def beautySum(self, s: str) -> int:
        outputSum = 0
        for i in range(len(s)):
            hashMap = defaultdict(int)
            for j in range(i, len(s)):
                
                hashMap[s[j]] += 1
                minfreq, maxfreq = self.getFreq(hashMap)
                outputSum += (maxfreq - minfreq)

        return outputSum
                
