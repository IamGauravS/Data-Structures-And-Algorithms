#
# @lc app=leetcode id=875 lang=python3
#
# [875] Koko Eating Bananas
#

# @lc code=start
import math 

class Solution:
    def calculateTime(self, piles, speed):
        totalTime = 0

        for banana in piles:
            time = math.ceil(banana/speed)
            totalTime += time 

        return totalTime

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles) > h:
            return -1 
        
        maxEatingSpeed = max(piles)
        minEatingSpeed = 1 

        while maxEatingSpeed > minEatingSpeed:
            speed = (maxEatingSpeed + minEatingSpeed)//2 

            if self.calculateTime(piles, speed) <= h:
                maxEatingSpeed = speed 

            else:
                minEatingSpeed = speed + 1


        return minEatingSpeed

        
# @lc code=end

