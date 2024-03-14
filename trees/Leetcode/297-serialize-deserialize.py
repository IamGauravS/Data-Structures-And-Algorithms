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
            return ''
        
        q = queue.Queue()
        q.put(root)
        output = []
        
        while not q.empty():
            curr = q.get()
            if curr:
                output.append(str(curr.val))
                q.put(curr.left)
                q.put(curr.right)
            else:
                output.append('#')
                
        return ','.join(output)
        
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        
        if data == '' or data == '#':
            return None 
        
        input_a = data.split(',')
        root = TreeNode(int(input_a[0]))
        q = queue.Queue()
        q.put(root)
        
        i = 1 
        
        while not q.empty and i < len(input_a):
            curr = q.get()
            
            if i < len(input_a) and input_a[i] != '#':
                curr.left = TreeNode(int(input_a[i]))
                q.put(curr.left)
                
            i+=1
            if i < len(input_a) and input_a[i] != '#':
                curr.right = TreeNode(int(input_a[i]))
                q.put(curr.right)
                
            i +=1
            
        return root 
        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))