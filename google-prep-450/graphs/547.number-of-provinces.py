#
# @lc app=leetcode id=547 lang=python3
#
# [547] Number of Provinces
#

# @lc code=start
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        visited  = set()
        def dfs(i):
            stack = []
            visited.add(i)
            stack.append(i)

            while stack:
                curr = stack.pop()
                for j in range(len(isConnected[0])):
                    if isConnected[curr][j] == 1 and j not in visited:
                        visited.add(j)
                        stack.append(j)

        
        noOfProvinces = 0

        for i in range(len(isConnected)):
            if i not in visited:
                dfs(i)
                noOfProvinces += 1

        return noOfProvinces


        
# @lc code=end

