class DisjointSet:

    def __int__(self, size: int):
        self.size, self.rank, self.parent = size, [], []
        for i in range(size+1):
            self.rank[i] = 0
            self.parent[i] = i

    def find(self, node: int):
        if node == self.parent[node]:
            return node
        else :
            self.parent[node] = self.find(self.parent[node])
            return self.parent[node]

    def union(self, u: int, v: int):
        u, v = self.find(u), self.find(v)
        if u == v:
            return False
        elif self.rank[u] == self.rank[v]:
            self.parent[u] = v
            self.rank[v] += 1
        else:
            self.parent[u if self.rank[u] < self.rank[v] else v] = v if self.rank[u] < self.rank[v] else u
