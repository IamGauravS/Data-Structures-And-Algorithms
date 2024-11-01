class Solution:
    def findCeil(self, root, inp):
        if root is None:
            return -1

        ceil = -1  # Initialize ceil as -1, assuming no valid ceil is found initially

        while root:
            if root.data == inp:
                return root.data  # Exact match, return immediately
            
            if inp < root.data:
                ceil = root.data  # Potential ceil found, move left to find a smaller valid ceil
                root = root.left
            else:
                root = root.right  # Move right if inp > root.data, as ceil might be larger

        return ceil
