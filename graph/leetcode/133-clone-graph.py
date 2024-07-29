"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node is None:
            return node

        visited = {}
        stack = [(node)]
        visited[node] = Node(node.val, [])

        while stack:
            oldnode = stack.pop()

            for n in oldnode.neighbors:
                if n not in visited:
                    visited[n] = Node(n.val, [])
                    stack.append(n)
                visited[oldnode].neighbors.append(visited[n])

        return visited[node]
            
            
            
            