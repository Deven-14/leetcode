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



from collections import defaultdict
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        adj = defaultdict(dict)

        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                d = abs(x2 - x1) + abs(y2 - y1)
                adj[i][j] = adj[j][i] = d
        
        min_heap = [(0, 0)]
        distance = 0
        visited = set()
        
        while len(visited) < n:
            curr_distance, i = heapq.heappop(min_heap)
            if i in visited:
                continue
            
            distance += curr_distance
            visited.add(i)

            for j, adj_distance in adj[i].items():
                if j in visited:
                    continue
                heapq.heappush(min_heap, (adj_distance, j))
                
        return distance
                


from collections import defaultdict
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        adj = [[0] * n for _ in range(n)]

        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                d = abs(x2 - x1) + abs(y2 - y1)
                adj[i][j] = adj[j][i] = d
        
        min_heap = [(0, 0)]
        distance = 0
        visited = set()
        
        while len(visited) < n:
            curr_distance, i = heapq.heappop(min_heap)
            if i in visited:
                continue
            
            distance += curr_distance
            visited.add(i)

            for j in range(n):
                if j in visited:
                    continue
                heapq.heappush(min_heap, (adj[i][j], j))
                
        return distance
                


from collections import defaultdict
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        adj = [[0] * n for _ in range(n)]

        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                d = abs(x2 - x1) + abs(y2 - y1)
                adj[i][j] = adj[j][i] = d
        
        min_heap = [(0, 0)]
        distances = [float('inf')] * n
        distance = 0
        visited = set()
        
        while len(visited) < n:
            curr_distance, i = heapq.heappop(min_heap)
            if i in visited:
                continue
            
            distance += curr_distance
            visited.add(i)

            for j in range(n):
                if j in visited or distances[j] < adj[i][j]:
                    continue
                distances[j] = adj[i][j]
                heapq.heappush(min_heap, (adj[i][j], j))
                
        return distance


from collections import defaultdict
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        min_heap = [(0, 0)]
        distances = [float('inf')] * n
        distance = 0
        visited = [False] * n
        count = 0
        
        while count < n:
            curr_distance, i = heapq.heappop(min_heap)
            if visited[i]:
                continue
            
            distance += curr_distance
            visited[i] = True
            count += 1
            x1, y1 = points[i]

            for j in range(n):
                if visited[j]:
                    continue
                adj_distance = abs(points[j][0] - x1) + abs(points[j][1] - y1)
                if distances[j] < adj_distance:
                    continue
                distances[j] = adj_distance
                heapq.heappush(min_heap, (adj_distance, j))
            
                
        return distance


