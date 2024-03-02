import heapq


def k_smallest_number(lists, k):

    # Replace this placeholder return statement with your code
    
    start = 0
    heap = []
    max_kth_element = 0
    pointer_list = [1 for i in range(len(lists))]
    
    ## add first element of each list to heap
    for i in range(len(lists)):
        if len(lists[i]) > 0:
            heapq.heappush(heap, [lists[i][0], i])
            
    while start <k and len(heap) > 0:
        curr_element = heapq.heappop(heap)
        max_kth_element = curr_element[0]
        start +=1 
        
        if pointer_list[curr_element[1]] < len(lists[curr_element[1]]):
            
            heapq.heappush(heap, [lists[curr_element[1]][pointer_list[curr_element[1]]], curr_element[1]])
            pointer_list[curr_element[1]] +=1 
            
            
    return max_kth_element
    