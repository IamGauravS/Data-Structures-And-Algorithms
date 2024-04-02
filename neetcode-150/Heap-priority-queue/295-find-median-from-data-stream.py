import heapq
class MedianFinder:

    def __init__(self):
        self.before_median = []  ## this will be a max heap so numbers will be stored as negative
        self.after_median = []  ## this will be a normal min heap

    def addNum(self, num: int) -> None:
        if len(self.before_median) == 0: ## if len(before_median) is zero we push in it
            heapq.heappush(self.before_median, -num)
        else:
            topElementBeforeMedian = -self.before_median[0]  ##check the top element of before median to determine the placement
            if num <= topElementBeforeMedian:  ## if its less then it will be in before median
                heapq.heappush(self.before_median, -num)
            else:
                heapq.heappush(self.after_median, num)
                
        if abs(len(self.after_median) - len(self.before_median)) > 1:
            if len(self.after_median) > len(self.before_median):
                topAfterMedianNum = heapq.heappop(self.after_median)
                heapq.heappush(self.before_median, -topAfterMedianNum)
            else:
                topBeforeMedianNum = -heapq.heappop(self.before_median)
                heapq.heappush(self.after_median, topBeforeMedianNum)
        return 
                
        

    def findMedian(self) -> float:
        
        totalElements = len(self.before_median) + len(self.after_median)
        if totalElements % 2 == 0 :
            topElementBeforeMedian = -self.before_median[0]
            topElementAfterMedian = self.after_median[0]
            return (topElementAfterMedian+ topElementBeforeMedian) / 2
        else:
            if len(self.before_median) > len(self.after_median):
                return -self.before_median[0]
            else:
                return self.after_median[0]        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()