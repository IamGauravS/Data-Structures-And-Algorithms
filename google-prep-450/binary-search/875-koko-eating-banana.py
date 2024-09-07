import math

class Solution:
    def getNoOfHours(self, speed):
        noOfHours = 0
        for pile in self.piles:
            noOfHours += math.ceil(pile/speed)

        return noOfHours

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        self.piles = piles 

        maxEatingSpeed = max(piles)
        minEatingSpeed = 1

        output = maxEatingSpeed

        while minEatingSpeed <= maxEatingSpeed:

            mid = (maxEatingSpeed + minEatingSpeed) // 2

            noOfHours = self.getNoOfHours(mid)

            if noOfHours <= h:
                output = mid
                maxEatingSpeed = mid - 1
                

            else:
                minEatingSpeed = mid + 1

        return output 
