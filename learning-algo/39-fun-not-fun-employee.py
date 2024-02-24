class Node:
    def __init__(self, fun, children=[]):
        self.fun = fun
        self.children = children

def max_fun(node, dp):
    if node is None:
        return 0

    if node in dp:
        return dp[node]

    # Calculate the maximum fun when the current employee (node) is included in the guest list
    include_fun = node.fun
    for child in node.children:
        for grandchild in child.children:
            include_fun += max_fun(grandchild, dp)

    # Calculate the maximum fun when the current employee (node) is excluded from the guest list
    exclude_fun = sum(max_fun(child, dp) for child in node.children)

    # Store the maximum fun in dp and return it
    dp[node] = max(include_fun, exclude_fun)
    return dp[node]

# Call the function max_fun(root) to start the algorithm with the company president as the root.
# root = Node(...)  # Initialize the company hierarchy tree with the president as the root
# dp = {}
# president_fun = root.fun + sum(max_fun(child, dp) for child in root.children)
# print(president_fun)