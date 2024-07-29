import random
class RandomSet():
    # Initialize your data structure here
    def __init__(self):
        # Write your code here
        self.location_dict = {}
        self.array = []
        self.size = 0

    # Inserts a value in the data structure
    # Returns True if it did not already contain the specified element
    def insert(self, val):
        # Write your code here
        if val in self.location_dict:
            return False 
        self.array.append(val)
        self.location_dict[val] = len(self.array) -1 
        self.size +=1
        return True

    # Removes a value from the data structure
    # Returns True if it contained the specified element
    def delete(self, val):
        if val not in self.location_dict:
            return False 
        idx = self.location_dict[val]
        if self.size - 1 != idx:
            last_element = self.array[self.size - 1]
            self.array[idx] = last_element
            self.location_dict[last_element] = idx  # Corrected this line
        self.array.pop()
        self.size -= 1
        del self.location_dict[val]
        return True  
        

    # Choose an element at random from the data structure.
    def get_random(self):
        # Write your code here
        random_idx = random.randint(0, self.size-1)
        return self.array[random_idx]