from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        self.numCourses = numCourses
        self.prerequisites = prerequisites
        
        self.AdjList = {}
        self.indegree = {} 
        
        for i in range(self.numCourses):
            self.AdjList[i] = []
            self.indegree[i] = 0
            
        for prequisite in self.prerequisites:
            a, b = prequisite[0], prequisite[1]
            self.AdjList[b].append(a)
            self.indegree[a] += 1
            
        coursesInOrder = [] 
        courseQueue = deque()
        
        for key in self.indegree:
            if self.indegree[key] == 0:
                courseQueue.append(key)
                
                
        while courseQueue:
            currCourse = courseQueue.popleft()
            coursesInOrder.append(currCourse)
            
            for children in self.AdjList[currCourse]:
                self.indegree[children] -=1 
                if self.indegree[children] == 0:
                    courseQueue.append(children)
                    
        if len(coursesInOrder) == self.numCourses:
            return coursesInOrder
        else:
            return []
        
        
## optimised

from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        AdjList = {i: [] for i in range(numCourses)}
        indegree = {i: 0 for i in range(numCourses)}
        
        for a, b in prerequisites:
            AdjList[b].append(a)
            indegree[a] += 1
            
        coursesInOrder = [] 
        courseQueue = deque(key for key in indegree if indegree[key] == 0)
                
        while courseQueue:
            currCourse = courseQueue.popleft()
            coursesInOrder.append(currCourse)
            
            for children in AdjList[currCourse]:
                indegree[children] -= 1 
                if indegree[children] == 0:
                    courseQueue.append(children)
                    
        return coursesInOrder if len(coursesInOrder) == numCourses else []