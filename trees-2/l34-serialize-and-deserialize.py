class Codec:
    def inorderTraversal(self, root):
        if root is None:
            return
        self.inorderTraversal(root.left)
        self.inorder.append(root.val)
        self.inorderTraversal(root.right)

    def preorderTraversal(self, root):
        if root is None:
            return
        self.preorder.append(root.val)
        self.preorderTraversal(root.left)
        self.preorderTraversal(root.right)

    def serialize(self, root):
        self.inorder = []
        self.preorder = []
        self.inorderTraversal(root)
        self.preorderTraversal(root)
        self.inorder = [str(val) for val in self.inorder]
        self.preorder = [str(val) for val in self.preorder]
        return ','.join(self.inorder) + '#' + ','.join(self.preorder)

    def deserialize(self, data):
        inorder, preorder = data.split('#')
        inorder = [int(val) for val in inorder.split(',') if val]
        preorder = [int(val) for val in preorder.split(',') if val]

        valueToIndexMap = {val: i for i, val in enumerate(inorder)}

        def helper(preorder, inorder):
            if not preorder or not inorder:
                return None 

            root = TreeNode(preorder[0])
            idx = valueToIndexMap[preorder[0]]

            inorder_left  = inorder[:idx]
            inorder_right = inorder[idx+1:]

            preorder_left = preorder[1: len(inorder_left)+1]
            preorder_right = preorder[len(inorder_left) + 1:]

            root.left = helper(preorder_left, inorder_left)
            root.right = helper(preorder_right, inorder_right)

            return root 

        return helper(preorder, inorder)