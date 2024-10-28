from collections import deque

class Solution:
    def topView(self, root):
        if not root:
            return []
        
        # Dictionary to store the first node at each horizontal distance
        top_view_map = {}
        
        # Queue to store nodes along with their horizontal distance from root
        queue = deque([(root, 0)])  # (node, horizontal_distance)
        
        while queue:
            node, hd = queue.popleft()
            
            # Store the node data if this horizontal distance hasn't been seen yet
            if hd not in top_view_map:
                top_view_map[hd] = node.data
            
            # Add left and right children to the queue with updated horizontal distances
            if node.left:
                queue.append((node.left, hd - 1))
            if node.right:
                queue.append((node.right, hd + 1))
        
        # Collecting the results in the order of horizontal distances from left to right
        sorted_hd = sorted(top_view_map.keys())
        return [top_view_map[hd] for hd in sorted_hd]
