def inorder_successor_helper(node, value, flag):
    if node is None:
        return None 

    left = inorder_successor_helper(node.left, value, flag)

    if left:
        return left

    if flag[0] and not flag[1]:
        flag[1] = True
        return node.data

    if node.data == value:
        flag[0] = True

    return inorder_successor_helper(node.right, value, flag)

def inorder_successor(root, value):
    flag = [False, False]  # [found_node, returned_successor]
    return inorder_successor_helper(root, value, flag)