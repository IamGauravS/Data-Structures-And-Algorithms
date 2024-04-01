
import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.capacity = k
        for num in nums:
            self.add(num)
                

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        
        if len(self.heap) > self.capacity:
            heapq.heappop(self.heap)
        return self.heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)