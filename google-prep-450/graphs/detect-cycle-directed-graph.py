class Solution:
    def hasCycle(self, i, pathVisited, visited, graph):
        pathVisited[i] = True 
        visited[i] = True 

        for neighbor in graph[i]:
            if pathVisited[neighbor] == True:
                return True 
            if visited[neighbor] == False:
                curr = self.hasCycle(neighbor, pathVisited, visited, graph)
                if curr:
                    return True 
                
        pathVisited[i] = False
        return False 

    def isCyclic(self, V: int, graph: List[List[int]]) -> bool:
        visited = {}  ## global visited
        pathVisited = {}  ## in that loop

        for i in range(V):
            visited[i] = False 
            pathVisited[i] = False

        for i in range(V):
            if visited[i] == False:
                if self.hasCycle(i, pathVisited, visited, graph):
                    return True 
                
        return False
        