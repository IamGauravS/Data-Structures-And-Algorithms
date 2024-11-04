#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#

# @lc code=start
from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        self.indegree = {}
        self.adjList = {}

        for i in range(numCourses):
            self.indegree[i] = 0
            self.adjList[i] = []

        for a, b in prerequisites:
            self.adjList[b].append(a)
            self.indegree[a] += 1

        queue = deque()
        for i in range(numCourses):
            if self.indegree[i] == 0:
                queue.append(i)

        coursesOrder = []
        while queue:
            currCourse = queue.popleft()
            coursesOrder.append(currCourse)
            for c in self.adjList[currCourse]:
                self.indegree[c] -= 1
                if self.indegree[c] == 0:
                    queue.append(c)

        return len(coursesOrder) == numCourses
        
# @lc code=end

