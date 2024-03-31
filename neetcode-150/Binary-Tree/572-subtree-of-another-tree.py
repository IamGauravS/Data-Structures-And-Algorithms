# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p == None and q == None:
            return True 
        if (p == None and  q != None) or (p != None and q == None) or p.val != q.val:
            return False
        
        isLeftSame = self.isSameTree(p.left, q.left)
        isRightSame = self.isSameTree(p.right, q.right)
        
        return isLeftSame and isRightSame
    
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None and subRoot is None:
            return True 
        
        if root is None or subRoot is None:
            return False
        
        if root.val == subRoot.val:
            isSame = self.isSameTree(root, subRoot)
            if isSame:
                return True 
            
        leftsame = self.isSubtree(root.left, subRoot)
        rightsame = self.isSubtree(root.right, subRoot)
        
        return leftsame or rightsame