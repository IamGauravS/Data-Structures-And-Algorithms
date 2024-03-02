import heapq

def compute_median(smaller_than_median_max_heap, greater_than_median_min_heap ):
    if len(smaller_than_median_max_heap) == len(greater_than_median_min_heap):
        return (-1*smaller_than_median_max_heap[0] + greater_than_median_min_heap[0])/2
    else:
        return -1*smaller_than_median_max_heap[0]
    
def balance(smaller_than_median_max_heap, greater_than_median_min_heap, outgoing_number):
    
    while len(greater_than_median_min_heap) > len(smaller_than_median_max_heap):
        temp = heapq.heappop(greater_than_median_min_heap)
        heapq.heappush(smaller_than_median_max_heap, -temp)
    
    while len(smaller_than_median_max_heap) - len(greater_than_median_min_heap) > 1:
        temp = - heapq.heappop(smaller_than_median_max_heap)
        heapq.heappush(greater_than_median_min_heap, temp) 
        
    if  -1* smaller_than_median_max_heap[0] in outgoing_number:
        if outgoing_number[-1* smaller_than_median_max_heap[0]] > 0:
            heapq.heappop(smaller_than_median_max_heap)
            outgoing_number[-1* smaller_than_median_max_heap[0]] -= 1
            balance(smaller_than_median_max_heap, greater_than_median_min_heap, outgoing_number)
        
    if  greater_than_median_min_heap[0] in outgoing_number:
        if outgoing_number[greater_than_median_min_heap[0]] > 0:
            heapq.heappop(greater_than_median_min_heap)
            outgoing_number[greater_than_median_min_heap[0]] -=1 
            balance(smaller_than_median_max_heap, greater_than_median_min_heap, outgoing_number)
    
    return smaller_than_median_max_heap, greater_than_median_min_heap, outgoing_number

def median_sliding_window(nums, k):

    # Replace this placeholder return statement with your code
    smaller_than_median_max_heap = []
    greater_than_median_min_heap = []
    outgoing_number = {}
    output = []
    
    for i in range(k):
        heapq.heappush(smaller_than_median_max_heap, -1*nums[i])
        
    for i in range(k/2):
        num = -1*heapq.heappop(smaller_than_median_max_heap)
        heapq.heappush(greater_than_median_min_heap, num) 
        
    output.append(compute_median(smaller_than_median_max_heap, greater_than_median_min_heap))
    
    for i in range(k, len(nums)):
        element_to_remove = nums[i-k]
        element_to_add = nums[i]
        
        if element_to_remove == -1* smaller_than_median_max_heap[0]:
            heapq.heappop(smaller_than_median_max_heap)
        
        elif element_to_remove == greater_than_median_min_heap[0]:
            heapq.heappop(greater_than_median_min_heap)
            
        else:
            if outgoing_number in element_to_remove:
                outgoing_number[element_to_remove] +=1
            else:
                outgoing_number[element_to_remove] = 1 
                
        if element_to_add < smaller_than_median_max_heap[0]:
            heapq.heappush(smaller_than_median_max_heap, -element_to_add)
        else:
            heapq.heappush(greater_than_median_min_heap, element_to_add)
            
        smaller_than_median_max_heap, greater_than_median_min_heap, outgoing_number =balance(smaller_than_median_max_heap, greater_than_median_min_heap, outgoing_number)
        
        output.append(compute_median(smaller_than_median_max_heap, greater_than_median_min_heap))
        
    return output