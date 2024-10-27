class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

class BinaryTree:
    def __init__(self, root_value):
        self.root = Node(root_value)

    def insert_left(self, current_node, value):
        if current_node.left is None:
            current_node.left = Node(value)
        else:
            new_node = Node(value)
            new_node.left = current_node.left
            current_node.left = new_node

    def insert_right(self, current_node, value):
        if current_node.right is None:
            current_node.right = Node(value)
        else:
            new_node = Node(value)
            new_node.right = current_node.right
            current_node.right = new_node

    # Depth-First Search Traversals
    def inorder_traversal(self, node, visited=None):
        if visited is None:
            visited = []
        if node:
            self.inorder_traversal(node.left, visited)
            visited.append(node.value)
            self.inorder_traversal(node.right, visited)
        return visited

    def preorder_traversal(self, node, visited=None):
        if visited is None:
            visited = []
        if node:
            visited.append(node.value)
            self.preorder_traversal(node.left, visited)
            self.preorder_traversal(node.right, visited)
        return visited

    def postorder_traversal(self, node, visited=None):
        if visited is None:
            visited = []
        if node:
            self.postorder_traversal(node.left, visited)
            self.postorder_traversal(node.right, visited)
            visited.append(node.value)
        return visited

    # Breadth-First Search Traversal
    def bfs(self):
        if not self.root:
            return []
        queue = [self.root]
        result = []
        while queue:
            current_node = queue.pop(0)
            result.append(current_node.value)
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
        return result
