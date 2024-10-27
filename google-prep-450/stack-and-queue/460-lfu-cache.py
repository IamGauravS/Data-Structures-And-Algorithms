class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.freq = 1  # Start with a frequency of 1
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = Node(0, 0)  # Dummy head
        self.tail = Node(0, 0)  # Dummy tail
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0  # Size of the list

    def add_to_front(self, node: Node):
        """Add a node to the front (most recently used)."""
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
        self.size += 1

    def remove(self, node: Node):
        """Remove a node from the list."""
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
        self.size -= 1

    def remove_last(self) -> Node:
        """Remove the last node (least recently used) and return it."""
        if self.size > 0:
            last_node = self.tail.prev
            self.remove(last_node)
            return last_node
        return None

class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.min_freq = 0  # Track the minimum frequency
        self.cache = {}  # Map from key to node (stores key, value, frequency)
        self.freq_map = {}  # Map from frequency to DoublyLinkedList of nodes
        self.size = 0  # Current size of the cache

    def update_freq(self, node: Node):
        """Helper function to update the frequency of a node."""
        # Remove the node from its current frequency list
        freq = node.freq
        self.freq_map[freq].remove(node)

        # If this frequency list is now empty, remove it and update min_freq
        if self.freq_map[freq].size == 0:
            del self.freq_map[freq]
            if self.min_freq == freq:
                self.min_freq += 1  # Increase the min_freq

        # Increment the node's frequency
        node.freq += 1

        # Add the node to the new frequency list
        new_freq = node.freq
        if new_freq not in self.freq_map:
            self.freq_map[new_freq] = DoublyLinkedList()
        self.freq_map[new_freq].add_to_front(node)

    def get(self, key: int) -> int:
        """Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1."""
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self.update_freq(node)  # Update the frequency of the node
        return node.value

    def put(self, key: int, value: int) -> None:
        """Insert a key-value pair into the cache. If the key already exists, update its value and frequency."""
        if self.capacity == 0:
            return

        if key in self.cache:
            # If key exists, update its value and frequency
            node = self.cache[key]
            node.value = value
            self.update_freq(node)
        else:
            # If the cache is full, evict the least frequently used item
            if self.size == self.capacity:
                # Evict from the min_freq list (least frequently used, and least recently used within that)
                lfu_list = self.freq_map[self.min_freq]
                lfu_node = lfu_list.remove_last()
                del self.cache[lfu_node.key]
                self.size -= 1

            # Create a new node
            new_node = Node(key, value)
            self.cache[key] = new_node

            # Add the new node to the frequency list for frequency 1
            if 1 not in self.freq_map:
                self.freq_map[1] = DoublyLinkedList()
            self.freq_map[1].add_to_front(new_node)

            # Reset min_freq to 1 since we just added a new node with freq 1
            self.min_freq = 1
            self.size += 1
