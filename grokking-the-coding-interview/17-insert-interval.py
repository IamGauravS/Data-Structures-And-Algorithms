def insert_interval(existing_intervals, new_interval):

  # Replace this placeholder return statement with your code
    flag = False
    for i in range(len(existing_intervals)):
      if existing_intervals[i][0] > new_interval[0]:
        existing_intervals.insert(i, new_interval)
        flag = True 
        
    if flag == False:
      existing_intervals.append(new_interval)
      return existing_intervals
    
    output = [existing_intervals[0]]
    for i in range(0, len(existing_intervals)):
      if output[-1][1] >= existing_intervals[i][0]:
        curr = output.pop()
        if curr[1] <= existing_intervals[i][1]:
          curr[1] = existing_intervals[i][1]
        output.append(curr)
      else:
        output.append(existing_intervals[i])


    return output