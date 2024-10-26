class Job:
    
    # Job class which stores profit and deadline.
    
    def __init__(self,profit=0,deadline=0):
        self.profit = profit
        self.deadline = deadline
        self.id = 0

class Solution:
    
    #Function to find the maximum profit and the number of jobs done.
    def JobScheduling(self,Jobs,n):
        
        maxDeadline = 0
        for job in Jobs:
            maxDeadline = max(maxDeadline, job.deadline)

        jobSlot = [-1]*maxDeadline

        Jobs.sort(key = lambda x: x.profit, reverse=True)

        jobCount = 0
        maxProfit = 0

        for job in Jobs:

            for j in range(min(maxDeadline, job.deadline)-1, -1, -1):
                if jobSlot[j] == -1:
                    jobSlot[j] = job.id
                    jobCount += 1
                    maxProfit += job.profit


        return jobCount, maxProfit

