#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#

# @lc code=start
from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0]*numCourses
        adjList = [[] for _ in range(numCourses)]

        for a, b in prerequisites:
            adjList[b].append(a)
            indegree[a] += 1

        queue = deque()
        topoCount = 0
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        while queue:
            currCourse = queue.popleft()
            topoCount += 1

            for dependencies in adjList[currCourse]:
                indegree[dependencies] -= 1
                if indegree[dependencies] == 0:
                    queue.append(dependencies)

        return topoCount == numCourses
        
# @lc code=end

