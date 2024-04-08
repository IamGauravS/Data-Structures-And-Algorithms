class Solution:
    def findPath(self, currLoc, dst, k, noOfStops, currCost):
        if currLoc == dst:
            if noOfStops <= k:
                self.mincost = min(self.mincost, currCost)
            return 
        
        if noOfStops > k:
            return 
        
        for neighbor in self.adjList[currLoc]:
            nextLoc, cost = neighbor
            if nextLoc not in self.visited:
                self.visited.add(nextLoc)
                self.findPath(nextLoc, dst, k, noOfStops+1, currCost+cost)
                self.visited.remove(nextLoc)
                
        return 
                
                       
        
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        self.visited = set()
        self.adjList = {i:[] for i in range(n)}
        
        for flight in flights:
            source, dest, cost = flight     
            self.adjList[source].append((dest, cost))
            
        self.mincost = float('inf')
        self.visited.add(src)
        self.findPath(src, dst, k, -1, 0)  ## source , destination, noOfStops, k, currCost
        
        return self.mincost  if self.mincost != float('inf') else -1       
    
    
    
## optimal solution using dijkstra

import heapq
class Solution:
            
        
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        self.adjList = {i:[] for i in range(n)}
        
        for flight in flights:
            source, dest, cost = flight     
            self.adjList[source].append((dest, cost))
            
        heap = []
        heapq.heappush(heap, (0, src, -1))  ## currCost, node, noOfStops
        
        stops = {i:float('inf') for i in range(n)}
        
        while heap:
            currCost, currLoc, noOfStops = heapq.heappop(heap)
            
            if stops[currLoc] < noOfStops or noOfStops > k:
                continue 
            
            if  currLoc == dst :
                return currCost
                
            stops[currLoc] = noOfStops
            
            for neighbor in self.adjList[currLoc]:
                
                    nextLoc, cost = neighbor
                    heapq.heappush(heap, (currCost+cost, nextLoc, noOfStops+1))
                    
                    
        return -1
                    
                