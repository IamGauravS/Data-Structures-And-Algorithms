class TreeNode:
    def __init__(self, value):
        self.value = value  # Node's value
        self.left = None  # Left child
        self.right = None  # Right child
        self.height = 1  # Height of the node

class AVLTree:
    def __init__(self):
        self.root = None  # Root node of the tree

    # Function to get the height of the node
    def height(self, node):
        if not node:
            return 0
        return node.height

    # Function to get the balance factor of the node
    def balance(self, node):
        if not node:
            return 0
        return self.height(node.left) - self.height(node.right)

    # Right rotation function
    def rotate_right(self, y):
        x = y.left
        T2 = x.right

        # Perform rotation
        x.right = y
        y.left = T2

        # Update heights
        y.height = 1 + max(self.height(y.left), self.height(y.right))
        x.height = 1 + max(self.height(x.left), self.height(x.right))

        # Return the new root
        return x

    # Left rotation function
    def rotate_left(self, x):
        y = x.right
        T2 = y.left

        # Perform rotation
        y.left = x
        x.right = T2

        # Update heights
        x.height = 1 + max(self.height(x.left), self.height(x.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))

        # Return the new root
        return y

    # Insert function
    def insert(self, node, value):
        # Perform the normal BST insertion
        if not node:
            return TreeNode(value)
        if value < node.value:
            node.left = self.insert(node.left, value)
        elif value > node.value:
            node.right = self.insert(node.right, value)
        else:
            return node

        # Update the height of the ancestor node
        node.height = 1 + max(self.height(node.left), self.height(node.right))

        # Get the balance factor
        balance = self.balance(node)

        # If the node is unbalanced, then try out the 4 cases
        # Left Left Case
        if balance > 1 and value < node.left.value:
            return self.rotate_right(node)

        # Right Right Case
        if balance < -1 and value > node.right.value:
            return self.rotate_left(node)

        # Left Right Case
        if balance > 1 and value > node.left.value:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)

        # Right Left Case
        if balance < -1 and value < node.right.value:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)

        return node

    # Delete function
    def delete(self, root, value):
        # Perform the normal BST deletion
        if not root:
            return root

        if value < root.value:
            root.left = self.delete(root.left, value)
        elif value > root.value:
            root.right = self.delete(root.right, value)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            temp = self.find_min_value_node(root.right)
            root.value = temp.value
            root.right = self.delete(root.right, temp.value)

        if root is None:
            return root

        # Update the height of the current node
        root.height = 1 + max(self.height(root.left), self.height(root.right))

        # Get the balance factor
        balance = self.balance(root)

        # If the node is unbalanced, then try out the 4 cases
        # Left Left Case
        if balance > 1 and self.balance(root.left) >= 0:
            return self.rotate_right(root)

        # Left Right Case
        if balance > 1 and self.balance(root.left) < 0:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)

        # Right Right Case
        if balance < -1 and self.balance(root.right) <= 0:
            return self.rotate_left(root)

        # Right Left Case
        if balance < -1 and self.balance(root.right) > 0:
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)

        return root

    # Function to find the node with minimum value
    def find_min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    # Function to insert a value in the AVL tree
    def insert_value(self, value):
        self.root = self.insert(self.root, value)

    # Function to delete a value in the AVL tree
    def delete_value(self, value):
        self.root = self.delete(self.root, value)

    # Function for inorder traversal of the tree
    def inorder_traversal(self, root):
        if root:
            self.inorder_traversal(root.left)
            print(root.value, end=' ')
            self.inorder_traversal(root.right)

    # Function to print the tree
    def print_tree(self):
        self.inorder_traversal(self.root)