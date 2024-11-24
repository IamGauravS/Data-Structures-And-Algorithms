#
# @lc app=leetcode id=332 lang=python3
#
# [332] Reconstruct Itinerary
#

# @lc code=start
from collections import defaultdict
class Solution:
    def findItineraryHelper(self, source, path):
        if len(path) == self.noOfTickets + 1:
            return True 
        
        if source not in self.adjList:
            return False 
        
        
        tempAdjList = list(self.adjList[source])

        for i, neighbor in enumerate(tempAdjList):
            if neighbor != -1:
                self.adjList[source][i] = -1
                path.append(neighbor)
                if self.findItineraryHelper(neighbor, path):
                    return True 
                self.adjList[source][i] = neighbor
                path.pop()

        return False 


    def findItineraryV2(self, tickets: List[List[str]]) -> List[str]:
        ## so that adjlist is made in sorted order
        tickets.sort()

        self.adjList = defaultdict(list)

        for source, destination in tickets:
            self.adjList[source].append(destination)

        self.noOfTickets = len(tickets)
        path = ["JFK"]
        source = "JFK"
        self.findItineraryHelper(source, path)

        return path 
    
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # Create an adjacency list and sort destinations lexicographically
        adjList = defaultdict(list)
        for source, destination in tickets:
            adjList[source].append(destination)
        
        # Sort each source's destinations in reverse order to pop from the end efficiently
        for source in adjList:
            adjList[source].sort(reverse=True)

        result = []

        def visit(airport):
            # Process all destinations from the current airport
            while adjList[airport]:
                next_airport = adjList[airport].pop()
                visit(next_airport)
            # Add the airport to the result once all its neighbors are processed
            result.append(airport)

        # Start the journey from "JFK"
        visit("JFK")

        # Reverse the result since we construct it in post-order
        return result[::-1]
    
    

        
# @lc code=end

