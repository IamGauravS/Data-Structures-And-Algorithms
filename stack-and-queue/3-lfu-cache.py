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
    
    
## get function gets the key ## put fucntions store and if capacity then removes the least frequently used
## if there are multiple guys which are least frequently used then remove lru

class LFUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.hash_map = {}
        self.freq_map = {}
        self.min_freq = 0
        self.linked_list = DoublyLinkedList()

    def get(self, key):
        if key not in self.hash_map:
            return -1
        node = self.hash_map[key]
        self.freq_map[node.key] += 1
        return node.value

    def put(self, key, value):
        if self.capacity <= 0:
            return
        if key in self.hash_map:
            node = self.hash_map[key]
            node.value = value
            self.freq_map[node.key] += 1
        else:
            if len(self.hash_map) == self.capacity:
                min_freq_keys = [k for k, v in self.freq_map.items() if v == self.min_freq]
                lru_key = min(min_freq_keys, key=lambda k: self.hash_map[k].prev.key)
                self.linked_list.remove(self.hash_map[lru_key])
                del self.hash_map[lru_key]
                del self.freq_map[lru_key]
            new_node = self.linked_list.insert_at_head(key, value)
            self.hash_map[key] = new_node
            self.freq_map[key] = 1
            self.min_freq = 1