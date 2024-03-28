from sortedcontainers import SortedList
class TimeMap:

    def __init__(self):
        self.data_dict = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.data_dict:
            self.data_dict[key] = SortedList()
        self.data_dict[key].add((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.data_dict:
            return ""
        
        values = self.data_dict[key]
        start = 0
        end = len(values) -1 
        output = ""
        
        while start <= end:
            mid = (start + end)//2
            if values[mid][0] <= timestamp:
                output = values[mid][1]
                start = mid + 1
            else:
                end = mid -1
                
        return output
        
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)


## optimised assuming the time stamp will always be in increasing order

class TimeMap:

    def __init__(self):
        self.data_dict = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.data_dict:
            self.data_dict[key] = []
        self.data_dict[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.data_dict:
            return ""
        
        values = self.data_dict[key]
        start = 0
        end = len(values) -1 
        output = ""
        
        while start <= end:
            mid = (start + end)//2
            if values[mid][0] <= timestamp:
                output = values[mid][1]
                start = mid + 1
            else:
                end = mid -1
                
        return output