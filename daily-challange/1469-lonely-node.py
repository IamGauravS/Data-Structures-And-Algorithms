# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:
        lonelyNodes = []
        stack = []
        stack.append(root)

        while stack:
            curr = stack.pop()
            leftChild =  curr.left
            rightChild = curr.right

            if leftChild == None and rightChild != None:
                lonelyNodes.append(rightChild.val)
            if rightChild == None and leftChild != None:
                lonelyNodes.append(leftChild.val)

            if leftChild:
                stack.append(leftChild)
            if rightChild:
                stack.append(rightChild)


        return lonelyNodes