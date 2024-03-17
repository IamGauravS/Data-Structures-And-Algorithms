

def no_of_platforms(starting_time, end_time):
    
    starting_time = sorted(starting_time)
    end_time = sorted(end_time)
    
    platforms = 0
    max_platforms = 0
    i = 0
    j = 0
    while i < len(starting_time) and j < len(end_time):
        if starting_time[i] < end_time[j]:
            platforms +=1 
            if platforms > max_platforms:
                max_platforms = platforms
            
            i+=1    
        else:
            platforms -=1 
            j+=1 
            
            
    return max_platforms