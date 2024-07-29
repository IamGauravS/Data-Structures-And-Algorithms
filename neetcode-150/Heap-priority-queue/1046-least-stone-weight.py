import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for stone in stones:
            heapq.heappush(heap, -stone)
            
        while len(heap) > 1:
            heavestStone = -heapq.heappop(heap)
            secondHeavestStone = -heapq.heappop(heap)
            
            newStoneWeight = heavestStone - secondHeavestStone
            
            if newStoneWeight != 0:
                heapq.heappush(heap, -newStoneWeight)
                
                
        return -heap[0] if len(heap) > 0 else 0