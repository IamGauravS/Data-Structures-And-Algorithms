class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        indexMap = {}

        for i, ch in enumerate(s):
            if ch not in indexMap:
                indexMap[ch] = []

            if len(indexMap[ch]) <= 1:
                indexMap[ch].append(i)

            if len(indexMap[ch]) == 2:
                indexMap[ch][1] = i


        

        intervals = []
        for key in indexMap.keys():
            if len(indexMap[key]) == 1:
                intervals.append([indexMap[key][0], indexMap[key][0]])
            else:
                intervals.append(indexMap[key])

        intervals = sorted(intervals)

        noOfIntervals = len(intervals)
        merged = [intervals[0]]
        for i in range(1, noOfIntervals):
            if merged[-1][1] >= intervals[i][0]:
                merged[-1][1] = max(merged[-1][1], intervals[i][1])
            else:
                merged.append(intervals[i])

        return [interval[1] - interval[0] + 1 for interval in merged]

## optimal
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_occurrence = {c: i for i, c in enumerate(s)}
        j = anchor = 0
        ans = []
        for i, c in enumerate(s):
            j = max(j, last_occurrence[c])  ## here we update j on each iteration so when j==i it means
            ## that last occurance of all the characters before that we smaller then the last occurance of current character
            if i == j:
                ans.append(i - anchor + 1)
                anchor = i + 1 ## start of new partition
        return ans