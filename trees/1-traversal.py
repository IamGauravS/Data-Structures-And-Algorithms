
## root, left, right
def preorder_traversal(root):
    if root is None:
        return
    print(root.data)
    
    preorder_traversal(root.left)
    preorder_traversal(root.right)
    
    return 



def inorder_traversal(root):
    if root is None:
        return 
    
    inorder_traversal(root.left)
    print(root.data)
    inorder_traversal(root.right)
    
    
def inorder_traversal(root):
    stack = []
    current = root

    while True:
        if current is not None:
            # Place pointer to a tree node on the stack before traversing the node's left subtree
            stack.append(current)
            current = current.left

        # Backtrack from the empty subtree and visit the node at the top of the stack; 
        # if the stack is empty, you're done
        elif(stack):
            current = stack.pop()
            print(current.data)

            # We have visited the node and its left subtree. Now, it's right subtree's turn
            current = current.right 
        else:
            break

    print()
    
def postorder_traversal(root):
    if root is None:
        return 
    postorder_traversal(root.left)
    postorder_traversal(root.right)
    print(root.data)
    
def postorder_traversal(root):
    if root is None:
        return

    stack1 = [root]
    stack2 = []

    while stack1:
        node = stack1.pop()
        stack2.append(node)

        if node.left:
            stack1.append(node.left)
        if node.right:
            stack1.append(node.right)

    while stack2:
        node = stack2.pop()
        print(node.data)
        
    
from collections import deque

def level_order_traversal(root):
    if root is None:
        return

    queue = deque([root])

    while queue:
        node = queue.popleft()
        print(node.data)

        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)