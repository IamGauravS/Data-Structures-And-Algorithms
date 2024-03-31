# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        def _buildTreeHelper(preorder, inorder, inorder_idx):
        
            if len(preorder) == 0 or len(inorder) == 0:
                return None 
            
            root = TreeNode(preorder[0])
            
            idx = inorder.index(preorder[0])
            
            inorder_left  = inorder[:idx]
            inorder_right = inorder[idx+1:]
            
            preorder_left = preorder[1: len(inorder_left)+1]
            preorder_right = preorder[len(inorder_left) + 1: ]
            
            root.left = _buildTreeHelper(preorder_left, inorder_left, inorder_idx)
            root.right = _buildTreeHelper(preorder_right, inorder_right, inorder_idx)
            
            return root 
        
        inorder_idx = {val: i for i, val in enumerate(inorder)}
        return _buildTreeHelper(preorder, inorder, inorder_idx)
    
    
    
## editorial solution

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:

        def array_to_tree(left, right):
            nonlocal preorder_index
            # if there are no elements to construct the tree
            if left > right: return None

            # select the preorder_index element as the root and increment it
            root_value = preorder[preorder_index]
            root = TreeNode(root_value)


            preorder_index += 1

            # build left and right subtree
            # excluding inorder_index_map[root_value] element because it's the root
            root.left = array_to_tree(left, inorder_index_map[root_value] - 1)
            root.right = array_to_tree(inorder_index_map[root_value] + 1, right)

            return root

        preorder_index = 0

        # build a hashmap to store value -> its index relations
        inorder_index_map = {}
        for index, value in enumerate(inorder):
            inorder_index_map[value] = index

        return array_to_tree(0, len(preorder) - 1)
    
    
