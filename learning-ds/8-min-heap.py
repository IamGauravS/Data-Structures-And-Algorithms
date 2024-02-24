import sys 

class MinHeap:

    def __init__(self, maxsize):

        self.maxsize = maxsize
        self.size = 0
        self.Heap = [0]*(self.maxsize+1)
        self.Heap[0] = -1* sys.maxsize
        self.FRONT = 1 

    def parent(self, i):
        return i//2

    def leftChild(self, i):
        return i*2
    def rightChild(self,i):
        return (i*2) + 1

    def isLeaf(self, i):
        return i*2 > self.size 

    def swap(self, fpos, spos):
        self.Heap[fpos], self.Heap[spos] = self.Heap[spos], self.Heap[fpos]

    def minHeapify(self, pos):
        if not self.isLeaf(pos):
            left_child = self.leftChild(pos)
            right_child = self.rightChild(pos)

            if right_child < len(self.Heap) and self.Heap[right_child] < self.Heap[left_child]:
                min_child = right_child
            else:
                min_child = left_child

            if self.Heap[pos] > self.Heap[min_child]:
                self.swap(pos, min_child)
                self.minHeapify(min_child)



    def insert(self, element):
        if self.size >= self.maxsize:
            return 

        self.size +=1
        self.Heap[self.size] = element

        current = self.size 

        while self.Heap[current] < self.Heap[self.parent(current)]:
            self.swap(current, self.parent(current))
            current = self.parent(current)
# To answer your question, if the new node is smaller than its parent but greater than its right sibling, it doesn't matter. The insert function only compares the new node with its parent, not with its siblings. As long as the new node is smaller than its parent, it will continue to move up the heap. Once it's larger than or equal to its parent, it will stop moving. This ensures that the heap property is maintained.
    def minHeap(self):

        for pos in range(self.size//2, 0, -1):
            self.minHeapify(pos)

# Sure, the minHeap function is used to build a min-heap from an array.

# Here's how it works:

# It starts from the middle of the array and goes to the beginning of the array. The reason for starting from the middle is that the second half of the array consists of leaf nodes (in a complete binary tree), and leaf nodes are already valid min-heaps.

# For each position, it calls the minHeapify function. The minHeapify function ensures that the subtree rooted at the current position is a min-heap. If the current node violates the min-heap property (i.e., it is larger than one of its children), it swaps the node with its smallest child and recursively heapifies the affected subtree.

# By the time it reaches the beginning of the array, all subtrees are min-heaps, and therefore the entire tree is a min-heap.

# This function is typically called after inserting all elements into the heap, to ensure that the resulting heap satisfies the min-heap property.
            
    def remove(self):

        popped = self.Heap[self.FRONT]
        self.Heap[self.FRONT] = self.Heap[self.size]
        self.size -= 1
        self.minHeapify(self.FRONT)
        return popped 
