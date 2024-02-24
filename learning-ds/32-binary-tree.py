# Define the TreeNode class
class TreeNode:
    def __init__(self, value):
        self.parent = None  # Pointer to the parent node
        self.value = value  # Value of the node
        self.left = None  # Pointer to the left child
        self.right = None  # Pointer to the right child

# Define the Binary Search Tree class
class BinarySearchTree:
    def __init__(self):
        self.root = None  # Initialize the root of the tree as None

    # Function to insert a new value into the BST
    def insert(self, value):
        new_node = TreeNode(value)  # Create a new TreeNode with the given value
        if self.root is None:  # If the tree is empty, set the new node as the root
            self.root = new_node
        else:
            current = self.root  # Start at the root
            while True:
                if value < current.value:  # If the new value is less than the current node's value, go left
                    if current.left is None:  # If left child doesn't exist, insert here
                        current.left = new_node
                        new_node.parent = current
                        break
                    else:
                        current = current.left  # Otherwise, move to the left child and repeat
                else:  # If the new value is greater than or equal to the current node's value, go right
                    if current.right is None:  # If right child doesn't exist, insert here
                        current.right = new_node
                        new_node.parent = current
                        break
                    else:
                        current = current.right  # Otherwise, move to the right child and repeat

    # Function to search for a value in the BST
    def search(self, value):
        current = self.root  # Start at the root
        while current is not None:  # While there are still nodes to consider...
            if value == current.value:  # If the current node's value matches the target, return True
                return True
            elif value < current.value:  # If the target value is less than the current node's value, go left
                current = current.left
            else:  # If the target value is greater than the current node's value, go right
                current = current.right
        return False  # If no match was found after checking the whole tree, return False

    def delete(self, value):
        self.root = self._delete(self.root, value)

    def _delete(self, node, value):
        if node is None:
            return node

        if value < node.value:
            node.left = self._delete(node.left, value)
        elif value > node.value:
            node.right = self._delete(node.right, value)
        else:
            # Node with only one child or no child
            if node.left is None:
                temp = node.right
                node = None
                return temp
            elif node.right is None:
                temp = node.left
                node = None
                return temp

            # Node with two children: get the inorder successor (smallest in the right subtree)
            temp = self._minValueNode(node.right)

            # Copy the inorder successor's content to this node
            node.value = temp.value

            # Delete the inorder successor
            node.right = self._delete(node.right, temp.value)

        return node

    def _minValueNode(self, node):
        current = node

        # loop down to find the leftmost leaf
        while(current.left is not None):
            current = current.left

        return current
    
    def fin_min(self):
        curr = self.root 
        if curr == None:
            return None 
        min = -1
        while curr:
            min = curr.value
            curr = curr.right

        return min

    def kth_max(self, k):
        # This function will perform the reverse in-order traversal
        def reverse_inorder(node):
            if node is None or self.count >= k:
                return
            reverse_inorder(node.right)
            self.count += 1
            if self.count == k:
                self.kth_max = node.value
                return
            reverse_inorder(node.left)

        self.count = 0
        self.kth_max = None
        reverse_inorder(self.root)
        if self.kth_max is None:
            return "There are less than k nodes in the tree"
        else:
            return self.kth_max

    def find_ancestors(self, value):
        current = self.root
        ancestors = []

        while current is not None:
            if current.value == value:
                return ancestors
            elif value < current.value:
                ancestors.append(current.value)
                current = current.left
            else:
                ancestors.append(current.value)
                current = current.right

        return None 


# Example usage:
bst = BinarySearchTree()
bst.insert(5)
bst.insert(3)
bst.insert(7)
bst.insert(2)
bst.insert(4)

print(bst.search(3))  # Output: True
print(bst.search(6))  # Output: False