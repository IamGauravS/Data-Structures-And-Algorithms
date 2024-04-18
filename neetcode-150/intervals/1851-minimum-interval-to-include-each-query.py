import heapq
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        sortedIntervals = sorted(intervals)

        minHeap = []
        res, i = {}, 0
        for q in sorted(queries):  ## create a copy of sorted queries
            while i < len(sortedIntervals) and sortedIntervals[i][0] <= q:
                l, r = sortedIntervals[i]
                heapq.heappush(minHeap, (r-l+1, r))
                i +=1

            while minHeap and minHeap[0][1] < q: ## pop invalid intervals
                heapq.heappop(minHeap)

            res[q] = minHeap[0][0] if minHeap else -1


        output = [res[q] for q in queries]
        return output
