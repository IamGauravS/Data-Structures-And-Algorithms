# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTreeHelper(self, preorder, inorder):
        if len(inorder) == 0 or len(preorder) ==0:
            return None

        root = TreeNode(preorder[0])
        
        inorderIndex = self.valueToIndexMap[preorder[0]]

        leftInorder = inorder[:inorderIndex]
        leftPreorder = preorder[1: len(leftInorder)+1]
        root.left = self.buildTreeHelper(leftPreorder, leftInorder)

        
        rightInorder = inorder[inorderIndex+1:]
        rightPreorder = preorder[len(leftInorder)+1:]
        root.right = self.buildTreeHelper(rightPreorder, rightInorder)

        return root

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(inorder) == 0:
            return None 

        self.valueToIndexMap = {}
        for i, val in enumerate(inorder):
            self.valueToIndexMap[val] = i

        return self.buildTreeHelper(preorder, inorder)



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        def helper(preorder, inorder):
            if len(preorder) == 0 or len(inorder) == 0:
                return None 
            
            root = TreeNode(preorder[0])
            
            idx = valueToIndexMap[preorder[0]]
            
            inorder_left  = inorder[:idx]
            inorder_right = inorder[idx+1:]
            
            preorder_left = preorder[1: len(inorder_left)+1]
            preorder_right = preorder[len(inorder_left) + 1: ]
            
            root.left = self.buildTree(preorder_left, inorder_left)
            root.right = self.buildTree(preorder_right, inorder_right)
            
            return root 


        valueToIndexMap = {}
        for i, val in enumerate(inorder):
            valueToIndexMap[val] = i
        return helper(preorder, inorder)