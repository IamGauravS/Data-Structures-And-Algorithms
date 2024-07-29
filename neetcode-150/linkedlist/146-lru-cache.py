class Node:
    def __init__(self, key = None, val = None, next = None):
        self.key = key
        self.val = val
        self.next = next
        
class LinkedList:
    def __init__(self):
        self.head = None 
        
    def add(self, key, val):
        newNode = Node(key, val, self.head)
        self.head = newNode
        return
    
    def remove(self, key):
        if self.head.key == key:
            self.head = self.head.next
            return 
        
        prev = None 
        curr = self.head
        
        
        while curr:
            if curr.key == key:
                prev.next = curr.next
                del curr 
                return 
            prev = curr 
            curr = curr.next 
            
            
        return 
    
    def remove_tail(self):
        curr = self.head 
        
        while curr.next:
            curr = curr.next 
            
        self.remove(curr.key)
        return curr.key
            

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.curr_capacity = 0
        self.hashmap = {}
        self.LList = LinkedList()

    def get(self, key: int) -> int:
        if key in self.hashmap:
            value = self.hashmap[key]
            self.LList.remove(key)
            self.LList.add(key, value)
            
            return value
        
        return -1

    def put(self, key: int, value: int) -> None:
            
        if key in self.hashmap:
            self.LList.remove(key)
        else:
            self.hashmap[key] = -1
            
        self.LList.add(key, value)
        self.hashmap[key] = value
        self.curr_capacity += 1
        
        if self.curr_capacity > self.capacity:
            key_to_be_removed = self.LList.remove_tail()
            del self.hashmap[key_to_be_removed]
            self.curr_capacity -= 1
        return

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)