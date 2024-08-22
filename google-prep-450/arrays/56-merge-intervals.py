from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort()
        result = []
        
        for interval in intervals:
            if len(result) == 0:
                result.append(interval)

            else:
                if result[-1][-1] >= interval[0]:
                    while len(result) > 0 and result[-1][-1] >= interval[0]:
                        intervalStart, intervalEnd = result.pop()

                    result.append([intervalStart, intervalEnd if intervalEnd > interval[1] else interval[1]])

                else:
                    result.append(interval)

            


        return result 

            

