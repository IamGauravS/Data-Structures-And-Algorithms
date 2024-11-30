#
# @lc app=leetcode id=774 lang=python3
#
# [774] Minimize Max Distance to Gas Station
#

# @lc code=start
class Solution:
    def getNoOfGasStations(self, stations, maxDistance):
        noOfStations = 0

        for i in range(1, len(stations)):
            diff = stations[i] - stations[i-1]
            noOfStations += int(diff/maxDistance)

        return noOfStations

    def minmaxGasDist(self, stations: List[int], k: int) -> float:
        if len(stations) == 1:
            return 10**-6
        start = 10**-6
        end = -float('inf')

        for i in range(1, len(stations)):
            end = max(end, stations[i] - stations[i-1])

        while end - start > 10**-6:
            mid = (start+end)/2

            noOfGasStations = self.getNoOfGasStations(stations, mid)

            if noOfGasStations > k:
                start = mid

            else:
                end = mid 

        return end

        
# @lc code=end

