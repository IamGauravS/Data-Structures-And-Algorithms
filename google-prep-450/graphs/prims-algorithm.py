import heapq
from typing import List, Tuple
from collections import defaultdict
def prims_algorithm(n: int, edges: List[Tuple[int, int, int]]) -> int:
    adjList = {}

    for src, dest, weight in edges:
        adjList[src].append((dest, weight))
        adjList[dest].append((src, weight))


    minHeap = [(0, 0, -1)]  ## weight, source node , parent
    visited = [0]*n 
    totalCost = 0
    mstEdges = []

    while minHeap:
        weight, currNode, parent  = heapq.heappop(minHeap)

        if visited[currNode]:
            continue

        totalCost += weight
        visited[currNode] = True 

        if parent != -1:
            mstEdges.append((currNode, parent, weight))

        for neighbor, edgeWeight in adjList[currNode]:
            if not visited[neighbor]:
                heapq.heappush(minHeap, (edgeWeight, neighbor, currNode))


    if all(visited):
        return totalCost, mstEdges
    else:
        return float('inf'), []





