class NodeInfo:
    def __init__(self, is_bst, size, min_val, max_val):
        self.is_bst = is_bst
        self.size = size
        self.min_val = min_val
        self.max_val = max_val

def find_largest_bst(root):
    def post_order(node):
        if not node:
            return NodeInfo(True, 0, float('inf'), float('-inf'))

        left_info = post_order(node.left)
        right_info = post_order(node.right)

        if left_info.is_bst and right_info.is_bst and left_info.max_val < node.data < right_info.min_val:
            is_bst = True
            size = left_info.size + right_info.size + 1
        else:
            is_bst = False
            size = max(left_info.size, right_info.size)

        min_val = min(left_info.min_val, node.data)
        max_val = max(right_info.max_val, node.data)

        return NodeInfo(is_bst, size, min_val, max_val)

    return post_order(root).size