
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
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
            
        count = 0 ## we only need to count
        stack = []
        
        for key in self.indegree:
            if self.indegree[key] == 0:
                stack.append(key)
                
                
        while stack:
            curr = stack.pop()
            count +=1
            
            for children in self.AdjList[curr]:
                self.indegree[children] -= 1
                if self.indegree[children] == 0:
                    stack.append(children)
                    
                    
        return count == self.numCourses
            
        
            
                
                
            