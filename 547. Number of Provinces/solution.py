class DisjointSetUnion:

    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.rank = [0] * n
        self.components = n
    
    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        
        return self.parents[x]
    
    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)

        if pu == pv:
            return False
        
        self.components -= 1
        if self.rank[pv] < self.rank[pu]:
            u, v = v, u
            pu, pv = pv, pu
        
        self.rank[pu] += self.rank[pv]
        self.parents[pv] = pu

        return True

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        dsu = DisjointSetUnion(n)

        for i, adj in enumerate(isConnected):
            for j, is_node_connected in enumerate(adj):
                if is_node_connected:
                    dsu.union(i, j)
        
        return dsu.components


class DisjointSetUnion:

    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.rank = [0] * n
        self.components = n
    
    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        
        return self.parents[x]
    
    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)

        if pu == pv:
            return False
        
        self.components -= 1
        if self.rank[pv] < self.rank[pu]:
            u, v = v, u
            pu, pv = pv, pu
        
        self.rank[pu] += self.rank[pv]
        self.parents[pv] = pu

        return True

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        dsu = DisjointSetUnion(n)

        for i, adj in enumerate(isConnected):
            for j in range(i, n):
                if adj[j]:
                    dsu.union(i, j)
        
        return dsu.components


class DisjointSetUnion:

    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.rank = [0] * n
        self.components = n
    
    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        
        return self.parents[x]
    
    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)

        if pu == pv:
            return False
        
        self.components -= 1
        if self.rank[pv] < self.rank[pu]:
            u, v = v, u
            pu, pv = pv, pu
        
        self.rank[pu] += self.rank[pv]
        self.parents[pv] = pu

        return True

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        dsu = DisjointSetUnion(n)

        for i, adj in enumerate(isConnected):
            for j in range(i+1, n):
                if adj[j]:
                    dsu.union(i, j)
        
        return dsu.components


class DisjointSetUnion:

    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.rank = [0] * n
        self.components = n
    
    def find(self, x):
        if self.parents[x] == x:
            return x
        
        px = self.parents[x]
        ppx = self.parents[px]
        if ppx == px:
            return px
        
        self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    
    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)

        if pu == pv:
            return False
        
        self.components -= 1
        if self.rank[pv] < self.rank[pu]:
            u, v = v, u
            pu, pv = pv, pu
        
        self.rank[pu] += self.rank[pv]
        self.parents[pv] = pu

        return True

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        dsu = DisjointSetUnion(n)

        for i, adj in enumerate(isConnected):
            for j in range(i+1, n):
                if adj[j]:
                    dsu.union(i, j)
        
        return dsu.components



class Solution:

    def dfs(self, isConnected, node, visited):
        visited[node] = True
        for adj_node, is_connected in enumerate(isConnected[node]):
            if is_connected and not visited[adj_node]:
                self.dfs(isConnected, adj_node, visited)

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [False] * n
        components = 0

        for node in range(n):
            if not visited[node]:
                self.dfs(isConnected, node, visited)
                components += 1

        return components
        