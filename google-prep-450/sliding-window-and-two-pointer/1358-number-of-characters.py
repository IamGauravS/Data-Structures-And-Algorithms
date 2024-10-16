class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        if k == len(cardPoints):
            return sum(cardPoints)

        prefixSum = [0]
        currSum = 0
        for point in cardPoints:
            currSum += point
            prefixSum.append(currSum)

        suffixSum = [0]
        currSum = 0
        for point in cardPoints[::-1]:
            currSum += point
            suffixSum.append(currSum)

        ## lets take all cards from back
        fromSuffix = k 
        fromPrefix = 0

        maxSum = -1
        while fromSuffix >= 0:
            maxSum = max(suffixSum[fromSuffix] + prefixSum[fromPrefix], maxSum)
            fromSuffix -= 1
            fromPrefix += 1

        return maxSum
    

## optimal way with same time complexity

from typing import List

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        total = sum(cardPoints[:k])
        maxSum = total

        for i in range(1, k + 1):
            total += cardPoints[-i] - cardPoints[k - i]
            maxSum = max(maxSum, total)

        return maxSum