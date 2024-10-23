class MinHeap:
    def __init__(self):
        self.heap = []

    def push(self, element):
        # Insert the new element
        self.heap.append(element)
        # Heapify up to maintain heap property
        self._heapify_up(len(self.heap) - 1)

    def pop(self):
        if len(self.heap) == 0:
            return None
        # Swap the root (min) with the last element
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        # Remove the last element (which is the minimum element)
        min_element = self.heap.pop()
        # Heapify down to restore heap property
        self._heapify_down(0)
        return min_element

    def top(self):
        # Return the smallest element without removing it
        if len(self.heap) == 0:
            return None
        return self.heap[0]

    def get(self):
        # Return the entire heap as a list
        return self.heap

    def _heapify_up(self, index):
        # Move up the element at index to its correct position
        parent = (index - 1) // 2
        if index > 0 and self.heap[index] < self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            self._heapify_up(parent)

    def _heapify_down(self, index):
        # Move down the element at index to its correct position
        left = 2 * index + 1
        right = 2 * index + 2
        smallest = index

        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left

        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._heapify_down(smallest)
