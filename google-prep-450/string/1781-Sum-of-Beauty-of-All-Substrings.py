from collections import defaultdict
class Solution:
   
    
    def beautySum(self, s: str) -> int:
        outputSum = 0
        for i in range(len(s)):
            hashMap = defaultdict(int)
            minfreq, maxfreq = float('inf'), float('-inf')
            for j in range(i, len(s)):
               
                hashMap[s[j]] += 1
                minfreq = min(minfreq, hashMap[s[j]])
                maxfreq = max(maxfreq, hashMap[s[j]])
                outputSum += (maxfreq - minfreq)

        return outputSum
                

