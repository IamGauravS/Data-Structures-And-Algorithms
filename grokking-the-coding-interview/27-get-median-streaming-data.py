import heapq
# Tip: You may use some of the code templates provided
# in the support files

class MedianOfStream:
    def __init__(self):
    
        self.smaller_then_median_heap = []
        self.gretaer_then_median_heap = []
        self.median = -1

  # This function should take a number and store it
    def insert_num(self, num):
    # Write your code here
        if self.median == -1:
            heapq.heappush(self.smaller_then_median_heap, -1*num)
            self.median = num
        elif num >= self.median:
            heapq.heappush(self.gretaer_then_median_heap, num)
            
            while len(self.gretaer_then_median_heap) > len(self.smaller_then_median_heap):
                temp = heapq.heappop(self.gretaer_then_median_heap)
                heapq.heappush( self.smaller_then_median_heap, -1*temp)

        else:
            heapq.heappush(self.smaller_then_median_heap, -1*num)
            
            while len(self.smaller_then_median_heap) - len(self.gretaer_then_median_heap) > 1:
                temp = heapq.heappop(self.smaller_then_median_heap)
                heapq.heappush(self.gretaer_then_median_heap, -1*temp)
                
        if len(self.smaller_then_median_heap) == len(self.gretaer_then_median_heap) and len(self.smaller_then_median_heap) > 0:
            self.median = (-1*self.smaller_then_median_heap[0] + self.gretaer_then_median_heap[0]) / 2 
        elif len(self.smaller_then_median_heap) > 0:
            self.median = -1*self.smaller_then_median_heap[0]

  # This function should return the median of the stored numbers
    def find_median(self):
    # Replace this placeholder return statement with your code
        return self.median
