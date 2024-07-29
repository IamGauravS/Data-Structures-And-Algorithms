class Solution:
    def __init__(self):
        self.ancestor = None

    def lowest_common_ancestor_helper(self, current_node, p, q):
        if current_node == None:
            return False

        left = self.lowest_common_ancestor_helper(current_node.left, p, q)
        right = self.lowest_common_ancestor_helper(current_node.right, p, q)
        mid = current_node.data == p or current_node.data == q

        if mid + left + right >= 2:
            self.ancestor = current_node

        return mid or left or right

    def lowest_common_ancestor(self, current_node, p, q):
        self.lowest_common_ancestor_helper(current_node, p, q)
        return self.ancestor