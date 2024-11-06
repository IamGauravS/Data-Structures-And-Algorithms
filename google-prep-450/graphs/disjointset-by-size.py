from collections import defaultdict

class UnionFind:
    """
    Implements Union-Find with path compression and union by size.
    """

    def __init__(self) -> None:
        self.parent = defaultdict(lambda: None)
        self.size = defaultdict(lambda: 1)  # Initialize size to 1 for each new node

    def find(self, node: int) -> int:
        """
        Finds and returns the root of the node, with path compression applied.

        Args:
            node (int): Node for which to find the root.

        Returns:
            int: The root of the node.
        """
        # Initialize the parent if the node is new
        if self.parent[node] is None:
            self.parent[node] = node

        # Apply path compression
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])

        return self.parent[node]
    
    def union(self, node1: int, node2: int) -> None:
        """
        Unites two nodes by their size, attaching the smaller tree under the larger.

        Args:
            node1 (int): The first node to unite.
            node2 (int): The second node to unite.
            
        Returns:
            None
        """
        root1 = self.find(node1)
        root2 = self.find(node2)

        if root1 != root2:
            # Union by size
            if self.size[root1] > self.size[root2]:
                self.parent[root2] = root1
                self.size[root1] += self.size[root2]
            else:
                self.parent[root1] = root2
                self.size[root2] += self.size[root1]
