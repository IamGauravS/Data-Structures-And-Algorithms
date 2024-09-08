import sys
class Solution:
    def flowersBloomed(self, adjacentFlowersRequired, noOfBouqetsRequired, currDay):
        tempBloomDay = self.bloomDay.copy()
        for i in range(len(self.bloomDay)):
            if tempBloomDay[i] <= currDay:
                tempBloomDay[i] = -1

        ## count number of bouqets possible
        currFlower = 0
        numOfBouqets = 0

        for i in range(len(self.bloomDay)):
            if tempBloomDay[i] == -1:
                currFlower += 1

            else:
                currFlower = 0

            if currFlower == adjacentFlowersRequired:
                numOfBouqets += 1
                currFlower = 0

            if numOfBouqets == noOfBouqetsRequired:
                return True 
            

        return False



    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m*k > len(bloomDay):
            return -1
        
        start = 1
        end = max(bloomDay)

        self.bloomDay = bloomDay
        adjacentFlowersRequired = k
        noOfBouqetsRequired = m

        minNumberOfDays = sys.maxsize

        while start <= end:
            mid = (start+end)//2

            if self.flowersBloomed(adjacentFlowersRequired, noOfBouqetsRequired, mid):
                minNumberOfDays = mid 
                end = mid - 1

            else:
                start = mid + 1


        return minNumberOfDays if minNumberOfDays != sys.maxsize else -1



## slightly optimised in terms of space

import sys
from typing import List

class Solution:
    def flowersBloomed(self, k: int, m: int, currDay: int) -> bool:
        currFlower = 0
        numOfBouqets = 0

        for day in self.bloomDay:
            if day <= currDay:
                currFlower += 1
                if currFlower == k:
                    numOfBouqets += 1
                    currFlower = 0
            else:
                currFlower = 0

            if numOfBouqets >= m:
                return True

        return False

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1
        
        start = 1
        end = max(bloomDay)

        self.bloomDay = bloomDay
        minNumberOfDays = sys.maxsize

        while start <= end:
            mid = (start + end) // 2

            if self.flowersBloomed(k, m, mid):
                minNumberOfDays = mid 
                end = mid - 1
            else:
                start = mid + 1

        return minNumberOfDays if minNumberOfDays != sys.maxsize else -1

# Example usage
solution = Solution()
print(solution.minDays([1, 10, 3, 10, 2], 3, 1))  # Output: 3



