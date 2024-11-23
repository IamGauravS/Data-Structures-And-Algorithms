#
# @lc app=leetcode id=981 lang=python3
#
# [981] Time Based Key-Value Store
#

# @lc code=start
from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.data = defaultdict(list)
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.data[key].append((timestamp, value))
        
    def get(self, key: str, timestamp: int) -> str:
        searchSpace = self.data[key]

        ## since the array is stored in a sorted order if the first element of the array is greater
        # then the required time then all the elements in the array is greater than the given time
        if not searchSpace or searchSpace[0][0] > timestamp:
            return ""

        left = 0
        right = len(searchSpace) - 1

        while left <= right:
            mid = (left + right)//2 

            if searchSpace[mid][0] <= timestamp:
                left = mid + 1
            else:
                right = mid-1 

        return searchSpace[right][1]
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
# @lc code=end

