import heapq

def kth_smallest_element(matrix, k):

    # Replace this placeholder return statement with your code
    
    kth_smallest_element = 0
    heap = []
    for i in range(len(matrix)):
        heapq.heappush(heap, [matrix[i][0], i, 0])
        
    curr = 0
    while heap and curr <k:
         curr_elem = heapq.heappop(heap)
         kth_smallest_element = curr_elem[0]
         i = curr_elem[1]
         position = curr_elem[2]
         
         if position+1 < len(matrix[i]):
             heapq.heappush(heap, [matrix[i][position+1], i, position+1])
        
         curr = curr+1
             
    return kth_smallest_element
        