

class RandomPickWithWeight:

    def __init__(self, weights):
        self.running_sum = []
        self.curr = 0
        for w in weights:
            self.curr += w 
            self.running_sum.append(self.curr)
        

    def pick_index(self):
        # Replace this placeholder return statement with your code
        random_number = random.randint(1, self.curr)
        high = len(self.running_sum) -1 
        low = 0
        while low <high:
            mid = (low+high)//2
            if self.running_sum[mid] < random_number:
                low = mid + 1
            else:
                high = mid
        return low
                
                
## By using low < high, we ensure that the loop stops when low and high point to the same index, which is the desired index. This is a common pattern when using binary search to find the smallest or largest index that satisfies a certain condition.