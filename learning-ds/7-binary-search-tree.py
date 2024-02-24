### binary search tree is a special case of binary tree which are ordered in a special way. 
### need to implement delete function here
class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data 
        self.left = None 
        self.right = None 

    def add_child(self, data):
        if data == self.data:  ## equal data is not allowed
            return 
        
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)

        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def inorder_traversal(self):
        queue = []

        if self.left:
            queue += self.left.inorder_traversal()

        queue.append(self.data)

        if self.right:
            queue += self.right.inorder_traversal()

        return queue


    def search(self, value):  ## here we use or operator implicitaly
        if self.data == value:
            return True 
        
        if value < self.data:
            if self.left:
                return self.left.search(value)
            else:
                return False
        
        else:
            if self.right:
                return self.right.search(value)
            else:
                return False

    def delete(self, value):
        if value < self.data:  # value is in the left subtree
            if self.left:
                self.left = self.left.delete(value)
        elif value > self.data:  # value is in the right subtree
            if self.right:
                self.right = self.right.delete(value)
        else:  # current node is the node to delete
            # Node with only one child or no child
            if not self.left:
                return self.right
            elif not self.right:
                return self.left

            # Node with two children, find the inorder successor
            temp = self.right
            while temp.left:
                temp = temp.left

            # Copy the inorder successor's data to this node
            self.data = temp.data

            # Delete the inorder successor
            self.right = self.right.delete(temp.data)

        return self  # return the (possibly updated) current node
    
    def all_greater_than(self, value): ## example or and operator
        if self.data <= value:
            return False

        left_subtree_result = True
        if self.left:
            left_subtree_result = self.left.all_greater_than(value)

        right_subtree_result = True
        if self.right:
            right_subtree_result = self.right.all_greater_than(value)

        return left_subtree_result and right_subtree_result


    
def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root 

if __name__ == '__main__':
    numbers = [17,4,1,20,9,23,18,34]
    numbers_tree = build_tree(numbers)
    print(numbers_tree.inorder_traversal())