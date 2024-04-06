class Solution:
    def dfs(self, key):
        self.visited[key] = True 
        for children in self.adjList[key]:
            if self.visited[children] == False:
                self.dfs(children)
                
        return 
    
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        self.visited = {}
        self.adjList = {}
        for i in range(n):
            self.visited[i] = False
            self.adjList[i] = []
            
            
        for edge in edges:
            self.adjList[edge[0]].append(edge[1])
            self.adjList[edge[1]].append(edge[0])
            
        no_of_components = 0
        for i in range(n):
            if self.visited[i] == False:
                no_of_components +=1 
                self.dfs(i)
                
        return no_of_components
        