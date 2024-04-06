import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        pointToNumberMap = {}
        
        adjList = {}
        
        for i, point in enumerate(points):
            pointToNumberMap[tuple(point)] = i
            
            adjList[i] = []
            
        visited = {}
        for i in range(len(points)):
            visited[i] = False
            
        
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                distance = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                adjList[pointToNumberMap[tuple(points[i])]].append((pointToNumberMap[tuple(points[j])], distance))
                adjList[pointToNumberMap[tuple(points[j])]].append((pointToNumberMap[tuple(points[i])], distance))
                
                
                
        minHeap = []
        minCost = 0
        minHeap.append([0,0])  ## distance, node 
        
        while minHeap:
            currDistance, node = heapq.heappop(minHeap)
            if visited[node] == False:  ## we put this check bcoz what if the new edge comes to something which we already visited
                ## before and we had a smaller edge for it
                visited[node] = True 
                minCost += currDistance
                for neighbor, distance in adjList[node]:
                    if visited[neighbor] == False:
                        heapq.heappush(minHeap, [distance, neighbor])
                    
                    
        return minCost
                
                
## kruskal's algorithm which uses union find

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def manhattan(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            parent[find(x)] = find(y)
        
        edges = []
        n = len(points)
        parent = list(range(n))
        for i in range(n):
            for j in range(i+1, n):
                edges.append((manhattan(points[i], points[j]), i, j))
        
        edges.sort()
        cost = 0
        noOfEdges = 0
        totalNoOfEdges = len(edges)
        for edge in edges:
            distance, i, j = edge
            if find(i) != find(j):
                cost += distance
                union(i, j)
                noOfEdges += 1
            if noOfEdges == totalNoOfEdges-1:
                break
        
        return cost
            
            
            