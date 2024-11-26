#
# @lc app=leetcode id=763 lang=python3
#
# [763] Partition Labels
#

# @lc code=start
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_occurrence = {c: i for i, c in enumerate(s)}
        j = anchor = 0
        ans = []
        for i, c in enumerate(s):
            j = max(j, last_occurrence[c])
            if i == j:
                ans.append(i - anchor + 1)
                anchor = i + 1
        return ans
    

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        firstAndLast = {}

        for i in range(len(s)):
            if s[i] not in firstAndLast:
                firstAndLast[s[i]] = [i,i]
            if s[i] in firstAndLast:
                    firstAndLast[s[i]][1] = i
                
        output = []
        firstAndLastItems = []
        for key, value in firstAndLast.items():
            firstAndLastItems.append(value)

        firstAndLastItems.sort()

        end = 0
        start = 0
        for elem in firstAndLastItems:
            
            currElemStart = elem[0]
            currElemEnd = elem[1] 

            if currElemStart <= end:
                end = max(currElemEnd, end)
            else:
                output.append(end-start+1)
                start = currElemStart
                end = currElemEnd 

        output.append(end-start+1)
        return output

        
# @lc code=end

