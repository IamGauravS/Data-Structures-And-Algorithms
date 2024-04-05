"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        if node == None:
            return None 
        
        duplicateSet  = {}
        stack = []
        visited = set()
        stack.append(node)
        
        while stack:
            curr = stack.pop()
            newNode = Node(curr.val)
            duplicateSet[curr] = newNode
            visited.add(curr)
            
            
            for neighbor in curr.neighbors:
                if neighbor not in visited:
                    stack.append(neighbor)
        
        for oldNode, newNode in duplicateSet.items():
            
            newNeighbors = []
            for neighbor in oldNode.neighbors:
                    newNeighbors.append(duplicateSet[neighbor])
                    
            newNode.neighbors = newNeighbors
                    
        return duplicateSet[node]
        
            
## optimised code

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None 

        duplicateSet = {node: Node(node.val)}
        stack = [node]

        while stack:
            curr = stack.pop()

            for neighbor in curr.neighbors:
                if neighbor not in duplicateSet:   ## we keep track of visited using this 
                    duplicateSet[neighbor] = Node(neighbor.val)
                    stack.append(neighbor)
                duplicateSet[curr].neighbors.append(duplicateSet[neighbor])

        return duplicateSet[node]
            
            
        