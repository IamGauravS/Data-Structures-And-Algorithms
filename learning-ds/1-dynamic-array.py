import ctypes
class dynamic_array(object):
    def __init__(self):

        self.len = 0  ## length of array what user thinks
        self.capacity = 1  ## actual array size
        self.arr = self.make_array(self.capacity)

    def __len__(self):
        return self.len 
    
    def __getitem__(self, k):
        
        if k >= 0 and k< self.len:
            return self.arr[k]
        else:
            return "Index out of Bounds"
        
    def append(self, element):
        if self.len == self.capacity:
            ## double the length of element
            self._resize(2*self.capacity)

        self.arr[self.len] = element
        self.len += 1

    def _resize(self, new_capacity):
        B = self.make_array(new_capacity)
        for i in range(self.len):
            B[i] = self.arr[i]
        self.arr = B
        self.capacity = new_capacity

    def make_array(self, new_capacity):
        return (new_capacity * ctypes.py_object)()
    



arr = dynamic_array()

print(len(arr))
arr.append("2")
arr.append(4)
arr.append("tut")
print(len(arr))
print(arr.capacity)
    
