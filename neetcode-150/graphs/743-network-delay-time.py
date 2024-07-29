import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjList = {}
        
        for i in range(1, n+1):
            adjList[i] = []
            
        for source, target, weight in times:
            adjList[source].append((target, weight))
            
        distance = {node : float('inf') for node in adjList}
        
        distance[k] = 0
        queue = [(0, k)]
        
        while queue:
            currDistance, currNode = heapq.heappop(queue)
            if currDistance != distance[currNode]:
                continue 
            
            for  neighbor, weight in adjList[currNode]:
                newDistance = currDistance + weight 
                
                if newDistance < distance[neighbor]:
                    distance[neighbor] = newDistance
                    heapq.heappush(queue, (newDistance, neighbor))
                    
        if any(dist == float('inf') for dist in distance.values()):
            return -1
        else:
            return max(distance.values())
            
            
