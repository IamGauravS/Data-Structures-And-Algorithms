import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        output_set = {}
        
        for num in nums:
            if num not in output_set:
                output_set[num] = 0
            output_set[num] += 1
            
        top_k_keys = sorted(output_set, key=output_set.get, reverse=True)[:k]
        
        return top_k_keys
    
    
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        output_set = {}
        
        for num in nums:
            if num not in output_set:
                output_set[num] = 0
            output_set[num] += 1
            
        heap = []
        
        for key, value in output_set.items():
            
            if len(heap) < k:
                
                heapq.heappush(heap, (value, key)) 
                
            else:
                if heap[0][0] < value:
                    heapq.heappop(heap)
                    heap.push(heap, (value, key))
                    
        
        output = []
        while heap:
            output.append(heapq.heappop(heap)[1])
            
        return output
    
    
    
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        output_set = {}
        
        for num in nums:
            if num not in output_set:
                output_set[num] = 0
            output_set[num] += 1
            
        freq = [[] for i in range(len(nums) + 1)]
        
        for n, c in output_set.items():
            freq[c].append(n)
            
        output = []
        
        for i in range(len(nums), -1, -1):
            for n in freq[i]:
                output.append(n)
                if len(output) == k:
                    return output
    
