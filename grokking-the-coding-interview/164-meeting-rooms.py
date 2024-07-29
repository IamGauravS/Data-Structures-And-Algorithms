def attend_all_meetings(intervals):

   # Replace this placeholder return statement with your code
   intervals = sorted(intervals, key = lambda x : x[0])
   
   for i in range(1, len(intervals)):
       if intervals[i-1][1] > intervals[i][0]:
           return False
       
   return True
       