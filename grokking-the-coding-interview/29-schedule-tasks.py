import heapq
import sys
def tasks(tasks_list):
    
    heap = []
    
    ## sort the tasks by start time
    tasks_list = sorted(tasks_list)
    no_of_machine = 0
    max_no_of_machine = -sys.maxsize
    
    for tasks in tasks_list:
        start_time = tasks[0]
        end_time = tasks[1]
        
        
        while len(heap) > 0 and heap[0] <= start_time :
            no_of_machine -= 1
            heapq.heappop(heap)
            
        heapq.heappush(heap, end_time)
        no_of_machine +=1
        if no_of_machine > max_no_of_machine:
            max_no_of_machine = no_of_machine
            
            
    return max_no_of_machine
                