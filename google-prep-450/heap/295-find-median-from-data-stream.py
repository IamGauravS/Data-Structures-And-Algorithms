import heapq
class MedianFinder:

    def __init__(self):
        self.leftside = []  ## max heap
        self.rightside = []  ## min heap

    def addNum(self, num: int) -> None:
        heapq.heappush(self.leftside, num)

        if len(self.leftside) - len(self.rightside) > 1:
            num = heapq.heappop(self.leftside)
            heapq.heappush(self.rightside, -num)

        return



    def findMedian(self) -> float:
        if len(self.leftside) == len(self.rightside):
            return (self.leftside[0] - self.rightside[0])//2
        else:
            return self.leftside[0]



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()