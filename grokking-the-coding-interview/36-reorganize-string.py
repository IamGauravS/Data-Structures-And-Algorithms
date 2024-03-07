from collections import Counter
import heapq

def reorganize_string(str):

    # Replace this placeholder return statement with your code
    str_frequency = Counter(str)
    
    str_freq_heap = []
    
    for key, value in str_frequency.items():
        heapq.heappush(str_freq_heap, [-value, key])
     
    output_str = ""   
    prev = [0, ""]
    while str_freq_heap:
        curr = heapq.heappop(str_freq_heap)
        char = curr[1]
        freq = -curr[0]
        if prev[0] > 0:
                heapq.heappush(str_freq_heap, [-prev[0], prev[1]]) 
        if freq > 1:
            prev = [freq-1, char]
        else:
            prev = [0, ""]
        output_str += char
        
    if len(output_str) != len(str):
        return ""
        
    return output_str
    