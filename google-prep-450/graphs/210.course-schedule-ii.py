#
# @lc app=leetcode id=210 lang=python3
#
# [210] Course Schedule II
#

# @lc code=start
from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        self.adjList = {}
        self.indegree = {}
        courseSchedule = []

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
                courseSchedule.append(i)

        while queue:
            course = queue.popleft()

            for neighbor in self.adjList[course]:
                self.indegree[neighbor] -= 1
                if self.indegree[neighbor] == 0:
                    courseSchedule.append(neighbor)
                    queue.append(neighbor)

        if len(courseSchedule) == numCourses:
            return courseSchedule
        return []


        
# @lc code=end

from collections import deque
from typing import List

def topological_sort_kahn(V: int, graph: List[List[int]]) -> List[int]:
    # Step 1: Calculate in-degrees of all vertices
    in_degree = [0] * V
    for u in range(V):
        for v in graph[u]:
            in_degree[v] += 1

    # Step 2: Initialize queue with nodes having in-degree 0
    queue = deque([i for i in range(V) if in_degree[i] == 0])
    topological_order = []

    # Step 3: Process nodes in topological order
    while queue:
        node = queue.popleft()
        topological_order.append(node)
        
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # Check for cycle: If topological order does not include all nodes, there's a cycle
    if len(topological_order) != V:
        return []  # Return empty list if a cycle is detected

    return topological_order



def topological_sort_dfs(V: int, graph: List[List[int]]) -> List[int]:
    visited = set()
    stack = []

    def dfs(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)
        stack.append(node)  # Append after visiting all descendants

    # Perform DFS for all unvisited nodes
    for i in range(V):
        if i not in visited:
            dfs(i)

    # Reverse the stack to get the correct topological ordering
    return stack[::-1]
