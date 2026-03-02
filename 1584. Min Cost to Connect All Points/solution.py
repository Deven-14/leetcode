class DisjointSetUnion:
    def __init__(self, n):
        self.parents = [-1] * n
        self.size = [1] * n
    
    def find(self, x):
        if self.parents[x] == -1:
            return x
        self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    
    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if px == py:
            return False
        
        if self.size[px] < self.size[py]:
            px, py = py, px
        
        self.parents[py] = px
        self.size[px] += self.size[py]
        return True

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edges = []
        n = len(points)

        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                edges.append((abs(x2 - x1) + abs(y2 - y1), i, j))
        
        edges.sort()

        dsu = DisjointSetUnion(n)
        distance = 0
        for d, u, v in edges:
            if dsu.union(u, v):
                distance += d
        
        return distance



class DisjointSetUnion:
    def __init__(self, n):
        self.parents = [-1] * n
        self.size = [1] * n
    
    def find(self, x):
        if self.parents[x] == -1:
            return x
        self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    
    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if px == py:
            return False
        
        if self.size[px] < self.size[py]:
            px, py = py, px
        
        self.parents[py] = px
        self.size[px] += self.size[py]
        return True

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edges = []
        n = len(points)

        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                edges.append((abs(x2 - x1) + abs(y2 - y1), i, j))
        
        edges.sort()

        dsu = DisjointSetUnion(n)
        distance = 0
        size = 0
        for d, u, v in edges:
            if dsu.union(u, v):
                distance += d
                size += 1
            if size == (n-1):
                break
        
        return distance
