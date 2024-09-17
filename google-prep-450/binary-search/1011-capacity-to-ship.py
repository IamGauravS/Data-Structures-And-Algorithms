class Solution:
    def countNumberOfDays(self, capacity):
        currLoad = 0
        numberOfDays = 0
        for weight in self.weights:
            currLoad += weight 
            if currLoad > capacity:
                numberOfDays += 1
                currLoad = weight

        if currLoad > 0:
            numberOfDays += 1

        return numberOfDays


    def shipWithinDays(self, weights: List[int], days: int) -> int:
        self.weights = weights 

        start = max(weights)
        end = sum(weights)

        outputNumberOfDays = end

        while start <= end:
            mid = (start + end) // 2

            if self.countNumberOfDays(mid) <= days:
                outputNumberOfDays = mid
                end = mid - 1

            else:
                start = mid + 1


        return outputNumberOfDays