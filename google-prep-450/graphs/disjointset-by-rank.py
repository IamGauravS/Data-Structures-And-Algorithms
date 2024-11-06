from collections import defaultdict

class UnionFind:
    """
    Implements Union-Find with path compression and union by rank.
    """

    def __init__(self):
        self.parent = defaultdict(lambda: None)  # Corrected lambda syntax
        self.rank = defaultdict(int)

    def find(self, node: int) -> int:
        """
        Finds and returns the root of the given node, applying path compression.

        Args:
            node (int): The node whose root is to be found.
            
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
        Unites two nodes by their rank, attaching the smaller tree under the larger one.

        Args:
            node1 (int): The first node to union.
            node2 (int): The second node to union.
            
        Returns:
            None
        """
        root1 = self.find(node1)
        root2 = self.find(node2)

        # Only unite if they have different roots
        if root1 != root2:
            # Union by rank
            if self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            elif self.rank[root2] > self.rank[root1]:
                self.parent[root1] = root2
            else:
                self.parent[root1] = root2
                self.rank[root2] += 1  
