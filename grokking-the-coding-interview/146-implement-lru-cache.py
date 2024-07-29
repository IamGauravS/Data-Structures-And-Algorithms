from linked_list import LinkedList


class LRUCache:
    # Initializes an LRU cache with the capacity size
    def __init__(self, capacity):
        self.cache_capacity = capacity
        self.cache_map = {}
        self.cache_list = LinkedList()

    # Returns the value of the key, or -1 if the key does not exist.
    def get(self, key):
        found_itr = None
        if key in self.cache_map:
            found_itr = self.cache_map[key]
        else:
            return -1

        list_iterator = found_itr
        self.cache_list.move_to_head(found_itr)

        return list_iterator.pair[1]

    # Adds a new key-value pair or updates an existing key with a new value
    def set(self, key, value):
        if key in self.cache_map:
            found_iter = self.cache_map[key]
            list_iterator = found_iter
            self.cache_list.move_to_head(found_iter)
            list_iterator.pair[1] = value
            return

        if len(self.cache_map) == self.cache_capacity:
            key_tmp = self.cache_list.get_tail().pair[0]
            self.cache_list.remove_tail()
            del self.cache_map[key_tmp]

        self.cache_list.insert_at_head([key, value])
        self.cache_map[key] = self.cache_list.get_head()