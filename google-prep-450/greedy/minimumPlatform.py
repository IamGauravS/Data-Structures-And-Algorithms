import heapq
class Solution:    
    #Function to find the minimum number of platforms required at the
    #railway station such that no train waits.
    def minimumPlatform(self,arr,dep):
        # code here
        
        schedule = []
        for a, d in zip(arr, dep):
            schedule.append((a, d))

        schedule = sorted(schedule, key = lambda x : x[0])

        noOfPlatForms = 1
        currTrains = [schedule[0][1]]

        for i in range(1, len(schedule)):
            currStart = schedule[i][0]

            while currTrains and currStart >= currTrains[0]:
                heapq.heappop(currTrains)

            heapq.heappush(currTrains, schedule[i][1])

            noOfPlatForms = max(noOfPlatForms, len(currTrains))


        return noOfPlatForms

