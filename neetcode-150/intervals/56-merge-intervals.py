class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sortedIntervals = sorted(intervals)

        result = []
        result.append(sortedIntervals[0])

        for i in range(len(sortedIntervals)):
            lastInterval = result[-1]

            if lastInterval[1] >= sortedIntervals[i][0]:
                lastInterval[1] = max(lastInterval[1], sortedIntervals[i][1])

            else:
                result.append(sortedIntervals[i])


        return result



