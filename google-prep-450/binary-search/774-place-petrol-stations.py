class Solution:
    def numberOfGasStationsRequired(self, maxDist: float) -> int:
        n = len(self.stations)
        cnt = 0
        for i in range(1, n):
            distance = self.stations[i] - self.stations[i - 1]
            numberInBetween = distance // maxDist
            if distance % maxDist == 0:
                numberInBetween -= 1
            cnt += int(numberInBetween)
        return cnt

    def minmaxGasDist(self, stations: List[int], k: int) -> float:
        self.stations = stations 
        distance = []
        for i in range(0, len(self.stations)-1):
            distance.append(self.stations[i+1] - self.stations[i])

        low = 0
        high = max(distance)
        maxDistance = high

        while (high-low) > 1e-6:
            mid = (low+high)/2.0

            count = self.numberOfGasStationsRequired(mid)

            if count <= k:
                high = mid 
                maxDistance = mid 

            else:
                low = mid 


        return maxDistance