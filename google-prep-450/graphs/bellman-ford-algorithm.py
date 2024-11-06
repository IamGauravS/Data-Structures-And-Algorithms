class Solution:
    def bellmanFord(self, n: int, edges: List[Tuple[int, int, int]], start: int) -> List[float]:
        distances = [float('inf')]*n 

        distances[start] = 0

        for _ in range(n-1):
            for u, v, w in edges:
                if distances[u] != float('inf'):
                    if distances[u] + w < distances[v]:
                        distances[v] = distances[u] + w 


        ## check for negative cycle 
        for u, v, w in edges:
            if distances[u] != float('inf') and distances[u] + w < distances[v]:
                print("negative cycle exsists")
                return []

        return distances