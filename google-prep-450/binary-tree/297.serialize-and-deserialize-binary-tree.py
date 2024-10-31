#
# @lc app=leetcode id=297 lang=python3
#
# [297] Serialize and Deserialize Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        
        def preorder(node):
            if not node:
                return ["#"]
            return [str(node.val)] + preorder(node.left) + preorder(node.right)
        
        return ','.join(preorder(root))

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def decode(nodes):
            val = next(nodes)
            if val == '#':
                return None 
            node = TreeNode(int(val))

            node.left = decode(nodes)
            node.right = decode(nodes)
            return node 
        
        nodes = iter(data.split(','))
        return decode(nodes)
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
# @lc code=end

