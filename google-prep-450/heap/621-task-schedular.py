import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        taskFreq = {}
        
        totalTime = 0

        for task in tasks:
            if task not in taskFreq:
                taskFreq[task] = 0
            taskFreq[task] += 1

        freqHeap = []
        

        for task, freq in taskFreq.items():
            heapq.heappush(freqHeap, -freq)

        while freqHeap:
            
            taskCount = 0
            cycle = n 
            store = []
            while cycle >= 0 and freqHeap:
                freq = -1*heapq.heappop(freqHeap)
                freq -= 1
                if freq > 0:
                    store.append(freq)
                cycle -= 1
                taskCount += 1

            while store:
                heapq.heappush(freqHeap, -store.pop())

            if not freqHeap:
                totalTime += taskCount
            else:
                totalTime += n + 1

        return totalTime

