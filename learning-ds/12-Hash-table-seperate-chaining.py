### hash table with seperate chaining and linked list
 
class Node:
    def __init__(self, key, value):
        self.key = key 
        self.value = value
        self.next = None 

class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.table = [None]*capacity

    def _hash_function(self, key):
        return hash(key) % self.capacity
    
    def insert(self, key, value):
        index = self._hash_function(key)

        if not self.table[index]:
            self.table[index] = Node(key, value)

        else:
            current = self.table[index]
            while current.next != None:
                current = current.next

            current.next = Node(key, value)

        
    def search(self, key):
        index = self._hash_function(key)

        current = self.table[index]
        while current:
            if current.key == key:
                return current.value 
            else:
                current = current.next 

        raise KeyError("key not found")
    
    def delete(self, key):
        index = self._hash_function(key)
        current = self.table[index]
        prev = None 

        while current:
            if current.key == key:
                if prev:
                    prev.next = current.next 
                else:
                    self.table[index] = current.next 

                return 
            
            prev = current 
            current = current.next 

if __name__ == '__main__':
    hash_table = HashTable(10)

    hash_table.insert("one", 1)
    hash_table.insert("two", 2)
    hash_table.insert("three", 3)

    print("Search 'one':", hash_table.search("one"))  # Output: 1
    print("Search 'four':", hash_table.search("four"))  # Raises KeyError

    hash_table.delete("two")
    print("Search 'two' after deletion:", hash_table.search("two"))