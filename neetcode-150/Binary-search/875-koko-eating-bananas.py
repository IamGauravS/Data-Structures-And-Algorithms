import math

class Solution:
    def calculate_no_of_hours(self, piles, mid):
        total_hours = 0
        for p in piles:
            total_hours += math.ceil(p/mid)
        return total_hours
    
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start = 1 
        end = max(piles)
        result = end 
        
        while start <= end:
            mid = (start + end) // 2
            no_of_hours = self.calculate_no_of_hours(piles, mid)
            
            if no_of_hours > h:
                start = mid + 1
            else:
                res = mid 
                end = mid - 1
            

        return res 