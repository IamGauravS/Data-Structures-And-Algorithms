class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        sortedPairs = sorted(pairs, key = lambda x : x[1])

        outputArray = [sortedPairs[0]]

        for pair in sortedPairs[1:]:
            if pair[0] < outputArray[-1][1]:
                outputArray.append(pair)

        return outputArray