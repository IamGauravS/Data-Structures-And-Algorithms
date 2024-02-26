## sort all the edges according to weight

from networkx.utils import UnionFind

def kruskal_algorithm(edges):
    uf = UnionFind()
    edges = sorted(edges, key = lambda edge: edge[2])
    mst = []
    for edge in edges:
        if uf[edge[0]] != uf[edge[1]]:
            uf.union(edge[0], edge[1])
            mst.append(edge)


    return mst
