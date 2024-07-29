import queue
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = {}
        
        indegree = [0 for i in range(numCourses)]
        
        for course in prerequisites:
            ai, bi = course 
            
            if bi not in adj_list:
                adj_list[bi] = []
                
            adj_list[bi].append(ai)
            indegree[ai] +=1
            
            
        topo = []
        
            
        q = queue.Queue()
        
        for i in range(numCourses):
            if indegree[i] == 0:
                q.put(i)
                
        while not q.empty():
            curr = q.get()
            topo.append(curr)
            
            if curr in adj_list:
                for ch in adj_list[curr]:
                    indegree[ch] -= 1
                    if indegree[ch] == 0:
                        q.put(ch)
                    
        
        if len(topo) == numCourses:
             return topo
        return []
                