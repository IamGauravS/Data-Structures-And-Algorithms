class MinHeapNode:
    def __init__(self, key):
        self.key = key 
        self.left = None 
        self.right = None 


class MinHeap:
    def __init__(self):
        self.root = None 

    def insert(self, key):
        if not self.root:
            self.root = MinHeapNode(key)
        else:
            self._insert(self.root, key)
    
    def _insert(self, root, key):
        if not root:
            return MinHeapNode(key)
        
        if key< root.key:
            root.key, key = key, root.key 
        
        if not root.left:
            root.left = MinHeapNode(key)
        elif not root.right:
            root.right = MinHeapNode(key)

        else:
            if root.left.key < root.right.key:
                self._insert(root.left, key)
            else:
                self._insert(root.right, key)

    
    def extrac_min(self):
        if not self.root:
            return None 
        
        min_value = self.root.key

        last_node_value = self._remove_last_node_value(self.root)
        self.root.key = last_node_value
        self.heapify_down(self.root)

        return min_value 
    
    def _remove_last_node_value(self, root):
        queue = [root]
        last_node = None 

        while queue:
            last_node = queue.pop[0]
            if last_node.left:
                queue.append(last_node.left)
            if last_node.right:
                queue.append(last_node.right)

        last_node_value = last_node.key 
        if last_node == self.root:
            self.root = None 

        ## delete the last node
        else:
            parent = self._find_parent_of_last_node(self.root, last_node)
            if parent.left == last_node:
                parent.left = None 
            else:
                parent.right = None 

        return last_node_value
    
    def _find_parent_of_last_node(self, root, last_node):
        queue = [root]

        while queue:
            current = queue.pop(0)
            if current.left == last_node or current.right == last_node:
                return current

            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

    def heapify_down(self, root):
        if not root:
            return

        left = root.left
        right = root.right
        smallest = root

        if left and left.key < smallest.key:
            smallest = left

        if right and right.key < smallest.key:
            smallest = right

        if smallest != root:
            root.key, smallest.key = smallest.key, root.key
            self.heapify_down(smallest)

    


    