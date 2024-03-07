from logs import *
from stack import *
from collections import deque

def exclusive_time(n, logs):

    # Replace this placeholder return statement with your code
    
   
            
    output = [0]* n
            
    stack = []
    
    for log in logs:
        log = Log(log)
        id = log.id
        status = log.is_start 
        time = log.time 
        
        if status == True:  ## log for starting
            stack.append(log)
        else:
            out_elem = stack.pop()
            start_time = out_elem.time 
            duration = time-start_time+1
            output[id] += duration 
            if stack:
                output[stack[-1].id] -= duration   ## here we are decreasing from duration of the previous id bcoz we shouldnt we counting
                ## the duration for which the current job ran to previous job
                
    return output
    
