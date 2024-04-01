import heapq

class Solution:
    def findDistance(self, x, y):
        return (x*x + y*y)**(1/2)
    
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        heap = []
        
        for point in points:
            distanceFromOrigin = self.findDistance(point[0], point[1])
            heapq.heappush(heap, (-distanceFromOrigin, point))
            
        while len(heap) > k:
            heapq.heappop(heap)
            
        return [point[1] for point in heap]
    
    
## optimnise since square is monotonic we do not need to do square root
## we can compare with max distance in heap which is on top and push only if it is less than max distance

class Solution:
    def findDistance(self, x, y):
        return x*x + y*y
    
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        heap = []
        
        for point in points:
            distanceFromOrigin = self.findDistance(point[0], point[1])
            if len(heap) < k:
                heapq.heappush(heap, (-distanceFromOrigin, point))
            else:
                if distanceFromOrigin < -heap[0][0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap, (-distanceFromOrigin, point))
                    
                    
            
            
        return [point[1] for point in heap]