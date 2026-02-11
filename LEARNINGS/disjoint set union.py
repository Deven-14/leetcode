class DisjointSetUnion:
    def __init__(self, n):
        self.parents = [-1] * n # or list(rnage(n))
        self.size = [0] * n
    
    def find(self, x):
        if self.parents[x] == -1: # or == x
            return x
        self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    
    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if px == py:
            return 
        
        if self.size[px] < self.size[py]:
            px, py = py, px
        
        self.parents[py] = px
        self.size[px] += self.size[py]