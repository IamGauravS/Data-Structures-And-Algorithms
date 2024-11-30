class Solution:
    def traverse(self, root):
        preorder = []
        postorder = []
        inorder = []

        stack = [(root, 1)]

        while stack:
            curr, ind = stack.pop()
            if ind == 1:
                preorder.append(curr.val)
                stack.append((curr, ind+1))
                if curr.left:
                    stack.append((curr.left, 1))

            elif ind == 2:
                inorder.append(curr.val)
                stack.append((curr, ind+1))
                if curr.right:
                    stack.append((curr.right, 1))

            else:
                postorder.append(curr.val)



        return preorder, postorder, inorder
    
    def preOrderTraversal(self, root):
        if not root:
            return []
        
        preorder = []
        stack = [root]

        while stack:
            curr = stack.pop()
            preorder.append(curr.val)
            if curr.right:
                stack.append(curr.right)
            # we add in reverse order
            if curr.left:
                stack.append(curr.left)

        return preorder
    
    def inorderTraversal(self, root):
        if not root:
            return []
        
        inorder = []
        stack = []
        curr = root 

        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            inorder.append(curr.val)
            curr = curr.right

        return inorder
    


                