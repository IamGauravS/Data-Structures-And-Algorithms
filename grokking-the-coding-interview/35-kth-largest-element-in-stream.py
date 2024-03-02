import heapq

class KthLargest:
    # Constructor to initialize heap and add values in it
    def __init__(self, k, nums):
        self.numbergreaterthank = []
        numbersmallerorequaltok = []
        
        for elem in nums:
            heapq.heappush(numbersmallerorequaltok, -elem)
            
        for i in range(k-1):
            temp = heapq.heappop(numbersmallerorequaltok)
            heapq.heappush(self.numbergreaterthank, -temp)
            
        self.kth_current = -numbersmallerorequaltok[0]
        

    # Adds element in the heap and return the Kth largest
    def add(self, val):

        # Replace this placeholder return statement with your code

       
       if val <= self.kth_current:
           return self.kth_current 
       
       if val > self.kth_current:
           heapq.heappush(self.numbergreaterthank, val)
           
       self.kth_current = heapq.heappop(self.numbergreaterthank)
       return self.kth_current