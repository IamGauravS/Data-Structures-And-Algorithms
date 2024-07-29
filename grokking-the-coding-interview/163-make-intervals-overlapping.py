def remove_min_intervals(intervals):

    # Replace this placeholder return statement with your code
    stack = []
    intervals = sorted(intervals, key = lambda x : x[0])
    
    for interval in intervals:
        if not stack or stack[-1][1] <= interval[0]:
            stack.append(interval)
            
    return len(intervals) - len(stack)