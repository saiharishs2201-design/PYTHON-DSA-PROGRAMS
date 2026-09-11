class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # path compression
        return self.parent[x]
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        if self.rank[px] < self.rank[py]:
            px, py = py, px
        self.parent[py] = px
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1
        return True

def kruskal_mst(n, edges):
    # edges: list of (weight, u, v)
    edges = sorted(edges)
    dsu = DSU(n)
    mst_weight = 0
    mst_edges = []
    
    for weight, u, v in edges:
        if dsu.union(u, v):
            mst_weight += weight
            mst_edges.append((u, v, weight))
    
    return mst_weight, mst_edges

edges = [(1, 0, 1), (3, 0, 2), (2, 1, 2), (4, 1, 3), (5, 2, 3)]
weight, mst = kruskal_mst(4, edges)
print("MST weight:", weight)
print("MST edges:", mst)