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
    def serializeHelper(self, root, output):
        if root == None:
            output.append("None")
            return 
        
        output.append(str(root.val))
        self.serializeHelper(root.left, output)
        self.serializeHelper(root.right, output)
        return 

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        output = []
        
        self.serializeHelper(root, output)

        outputStr = "##".join(output)
        return outputStr

    def deserializeHelper(self, dataList, index):
        if dataList[index[0]] == "None":
            index[0] += 1
            return None 

        root = TreeNode(int(dataList[index[0]]))
        index[0] += 1
        root.left = self.deserializeHelper(dataList, index)
        root.right = self.deserializeHelper(dataList, index)
        return root     

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """

        dataList = data.split('##')
        return self.deserializeHelper(dataList, [0])
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
# @lc code=end

