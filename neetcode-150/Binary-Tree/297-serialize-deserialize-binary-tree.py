# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import queue
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return "None"
        curr_str = ""
        q = queue.Queue()
        q.put(root)
        
        while not q.empty():
            curr = q.get()
            if curr != None:
                curr_str = curr_str + " " + str(curr.val)
            else:
                curr_str = curr_str + " " + "None"
                
            if curr:
                q.put(curr.left)
                q.put(curr.right)
                
        ## remove the extra space
        curr_str = curr_str[1:]
        return curr_str
        
        
        
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == "None":
            return None
        
        data = data.split(" ")
        
        root = TreeNode(val = int(data[0]))
        q = queue.Queue()
        q.put(root)
        i = 1
        
        while not q.empty() and i < len(data):
            curr = q.get()
            
            if i < len(data) and data[i] != "None":
                curr.left = TreeNode(val = int(data[i]))
                q.put(curr.left)
            i +=1
            
            if i < len(data) and data[i] != "None":
                curr.right = TreeNode(val = int(data[i]))
                q.put(curr.right)
            i +=1
            
        return root 
                
            

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))