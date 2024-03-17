## put, get put puts in cache and get gets if present if capacity is full then u remove the least recently used 
## 


class Node:
    def __init__(self, key=None, value=None, prev=None, next=None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next

class DoublyLinkedList:
    def __init__(self):
        self.head = Node()  # sentinel head node
        self.tail = Node()  # sentinel tail node
        self.head.next = self.tail
        self.tail.prev = self.head

    def insert_after(self, ref_node, key, value):
        new_node = Node(key, value)
        new_node.prev = ref_node
        new_node.next = ref_node.next
        ref_node.next.prev = new_node
        ref_node.next = new_node
        return new_node

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        
    def insert_at_head(self, key, value):
        return self.insert_after(self.head, key, value)
    
    
    
class LRUCache:
    def __init__(self, capacity):
        self.hash_map = {}
        self.linked_list = DoublyLinkedList()
        self.capacity = capacity
        
    def insert(self, key, value):
        
        if key in self.hash_map:
            node = self.hash_map[key]
            self.linked_list.remove(node)
            
        else:
            
            if len(self.hash_map) == self.capacity:
                tail_node = self.linked_list.remove_tail()
                del self.hash_map[tail_node.key]
                
        new_node = self.linked_list.insert_at_head(key, value)
        self.hash_map[key] = new_node
        
    
    def get(self, key):
        if key in self.hash_map:
            value = self.hash_map[key].value 
            
            node = self.hash_map[key]
            self.linked_list.remove(node)
            new_node= self.linked_list.insert_at_head(key, value)
            self.hash_map[key] = new_node
        else:
            return -1