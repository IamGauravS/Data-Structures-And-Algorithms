class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def _hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash_function(key)

        # Linear probing to find the next available slot
        while self.table[index] is not None:
            index = (index + 1) % self.size

        self.table[index] = (key, value)

    def search(self, key):
        index = self._hash_function(key)

        # Linear probing to find the key
        while self.table[index] is not None:
            stored_key, value = self.table[index]
            if stored_key == key:
                return value
            index = (index + 1) % self.size

        # Key not found
        raise KeyError(f"Key '{key}' not found")

    def delete(self, key):
        index = self._hash_function(key)

        # Linear probing to find the key
        while self.table[index] is not None:
            stored_key, _ = self.table[index]
            if stored_key == key:
                self.table[index] = None
                return
            index = (index + 1) % self.size

        # Key not found
        raise KeyError(f"Key '{key}' not found")

# Example usage
if __name__ == '__main__':
    hash_table = HashTable(size=10)

    # Insert some key-value pairs
    hash_table.insert("one", 1)
    hash_table.insert("two", 2)
    hash_table.insert("three", 3)

    # Search for a key
    print("Value for 'two':", hash_table.search("two"))

    # Delete a key
    hash_table.delete("two")

    # Attempt to search for the deleted key (raises KeyError)
    # print(hash_table.search("two"))  # Uncommenting this line will raise KeyError
