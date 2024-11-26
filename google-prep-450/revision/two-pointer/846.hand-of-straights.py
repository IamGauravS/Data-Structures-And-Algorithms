#
# @lc app=leetcode id=846 lang=python3
#
# [846] Hand of Straights
#

# @lc code=start
import heapq
from collections import defaultdict
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        freqDict = defaultdict(int)

        for card in hand:
            freqDict[card] += 1

        heap = []
        for key, value in freqDict.items():
            heapq.heappush(heap, (key, value))

        while heap:
            currMin , currFreq = heapq.heappop(heap)
            temp = []
            for i in range(currMin+1, currMin+groupSize):
                if not heap:
                    return False
                next, nextFreq = heapq.heappop(heap)
                if next != i or nextFreq < currFreq:
                    return False
                if nextFreq > currFreq:
                    temp.append((next, nextFreq - currFreq))

            for elem in temp:
                heapq.heappush(heap, elem)

        return True 
        
# @lc code=end

