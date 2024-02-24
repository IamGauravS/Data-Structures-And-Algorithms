class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, val):
        self.heap.append(val)
        self.__percolateUp(len(self.heap) -1)

    def getMax(self):
        return self.heap[0]

    def removeMax(self):
        if len(self.heap) == 0:
            return None 
        
        
        max = self.heap[0]
        self.heap[0] = self.heap[-1]
        del self.heap[-1]
        if len(self.heap) >0:
            self.__maxHeapify(0)
        
        return max

    def __percolateUp(self, index):
        if index == 0:
            return 
        if index % 2 == 0:
            parent = index //2 -1
        else:
            parent = index //2 

        if self.heap[parent] < self.heap[index]:
            self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
            return self.__percolateUp(parent)

    def __maxHeapify(self, index):
        rightchild = index*2 + 1
        leftchild = index*2 + 2

        largest = index 
        if leftchild < len(self.heap) and self.heap[leftchild] > self.heap[largest]:
            largest = leftchild
        if rightchild < len(self.heap) and self.heap[rightchild] > self.heap[largest]:
            largest = rightchild

        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self.__maxHeapify(largest)
        




heap = MaxHeap()


## convert max heap to min heap

def minHeapify(heap, index):
    left = index * 2 + 1
    right = (index * 2) + 2
    smallest = index
    # check if left child exists and is less than smallest
    if len(heap) > left and heap[smallest] > heap[left]:
        smallest = left
    # check if right child exists and is less than smallest
    if len(heap) > right and heap[smallest] > heap[right]:
        smallest = right
    # check if current index is not the smallest
    if smallest != index:
        # swap current index value with smallest
        tmp = heap[smallest]
        heap[smallest] = heap[index]
        heap[index] = tmp
        # minHeapify the new node
        minHeapify(heap, smallest)
    return heap


def convertMax(maxHeap):
    # iterate from middle to first element
    # middle to first indices contain all parent nodes
    for i in range((len(maxHeap))//2, -1, -1):
        # call minHeapify on all parent nodes
        maxHeap = minHeapify(maxHeap, i)
    return maxHeap