from collections import Counter
import heapq
def top_k_frequent(arr, k):

    # Replace this placeholder return statement with your code
    elem_count = Counter(arr)
    
    freq_max_heap = []
    for key, value in elem_count.items():
        heapq.heappush(freq_max_heap, [-value, key])
        
    output_list = []
    for i in range(k):
        curr = heapq.heappop(freq_max_heap)
        output_list.append(curr[1])
        
    return output_list
    