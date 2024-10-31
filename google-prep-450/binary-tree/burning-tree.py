from collections import defaultdict, deque

class Solution:
    def minTime(self, root, target):
        # Step 1: Build the neighbors graph
        neighbors = defaultdict(list)
        
        # Helper function to construct the graph
        def buildGraph(node):
            if not node:
                return
            if node.left:
                neighbors[node].append(node.left)
                neighbors[node.left].append(node)
                buildGraph(node.left)
            if node.right:
                neighbors[node].append(node.right)
                neighbors[node.right].append(node)
                buildGraph(node.right)
                
        buildGraph(root)
        
        # Step 2: Locate the target node
        def findTargetNode(node, target):
            if not node:
                return None
            if node.data == target:
                return node
            left = findTargetNode(node.left, target)
            return left if left else findTargetNode(node.right, target)
        
        targetNode = findTargetNode(root, target)
        
        # Step 3: BFS traversal to find the maximum distance
        queue = deque([(targetNode, 0)])
        visited = set([targetNode])
        maxDistance = 0

        while queue:
            currNode, distance = queue.popleft()
            maxDistance = max(maxDistance, distance)
            
            for neighbor in neighbors[currNode]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, distance + 1))

        return maxDistance
