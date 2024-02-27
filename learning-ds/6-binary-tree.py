class Node:
    def __init__(self, value):
        self.data = value
        self.left = None 
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None 

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)

        else:
            ## this inserts element from left to right using BFS method
            queue = [self.root]
            while queue:
                current = queue.pop(0)
                if current.left is None:
                    current.left = Node(data)
                    break 
                else:
                    queue.append(current.left)

                if current.right is None:
                    current.right = Node(data)
                    break 
                else:
                    queue.append(current.right)

    def search(self, data):

        if self.root is None:
            return False 
        
        queue = [self.root]
        
        while queue:
            current = queue.pop(0)
            if current.data == data:
                return True 
            
            if current.left is not None:
                queue.append(current.left)
            if current.right is not None:
                queue.append(current.right)

        return False
    
    def delete(self, data):

        if self.root is None:
            return "Tree is empty"
        
        ## find the node to be deleted
        key_node = None 
        queue = [self.root]

        while queue:
            temp = queue.pop(0)
            if temp.data == data:
                key_node = temp 
                ## here we do not break the loop because we temp to reach the deepest right most node
            if temp.left:
                queue.append(temp.left)
            if temp.right:
                queue.append(temp.right)

        if key_node:
            x = temp.data
            self.deleteDeepest(temp)
            key_node.data = x 

        else:
            return "data not found"

    def deleteDeepest(self, d_node):
        q = [self.root]
        while len(q):
            temp = q.pop(0)
            if temp is d_node:
                temp = None
                return 
            
            if temp.right:
                if temp.right is d_node:
                    temp.right = None
                    return 
            else:
                q.append(temp.right)

            if temp.left:
                if temp.left is d_node:
                    temp.left = None 
                    return 
                else:
                    q.append(temp.left)
            
    def inorder_traversal(self,node):
        if node is not None:
            self.inorder_traversal(node.left)
            print(node.data)
            self.inorder_traversal(node.right)

    def preorder_traversal(self, node):
        if node is not None:
            print(node.data)
            self.preorder_traversal(node.left)
            self.preorder_traversal(node.right)

    def level_order_traversal(self):
        if self.root is None:
            return

        queue = [self.root]
        while queue:
            current = queue.pop(0)
            print(current.data)

            if current.left is not None:
                queue.append(current.left)
            if current.right is not None:
                queue.append(current.right)


# Create a binary tree
bt = BinaryTree()

# Insert nodes
bt.insert(1)
bt.insert(2)
bt.insert(3)
bt.insert(4)
bt.insert(5)

# Search for a value
print(bt.search(3))  # Should print True
print(bt.search(6))  # Should print False

# Perform in-order traversal
bt.inorder_traversal(bt.root)  # Should print 4 2 5 1 3

# Delete a node
print(bt.delete(3))  # Should print "Deleted"
print(bt.search(3))  # Should print False

# Perform in-order traversal after deletion
bt.inorder_traversal(bt.root)  # Should print 4 2 5 1

# Perform level order traversal
bt.level_order_traversal()
                

