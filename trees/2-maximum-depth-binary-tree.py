def find_maximum_depth(root):
    if root == None:
        return 0 
    
    max_height = 1 + max(find_maximum_depth(root.left), find_maximum_depth(root.right))
    return max_height



## use bfs or level order if we want to do it iteratively
from collections import deque

def find_maximum_depth(root):
    if root is None:
        return 0

    queue = deque([(root, 1)])

    while queue:
        node, depth = queue.popleft()

        if node.left is not None:
            queue.append((node.left, depth + 1))
        if node.right is not None:
            queue.append((node.right, depth + 1))

    return depth