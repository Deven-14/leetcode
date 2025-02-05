class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        heights = {}
        adj = [[] for _ in range(n)]

        for (a, b) in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        def dfs(vertice, visited):
            if visited[vertice]:
                return 0
            
            visited[vertice] = True
            height = 0
            for neighbor in adj[vertice]:
                height = max(height, dfs(neighbor, visited))
            
            return 1 + height
        
        min_height = n+1
        min_height_vertices = []
        for vertice in range(n):
            visited = [False] * n
            height = dfs(vertice, visited)

            if min_height == height:
                min_height_vertices.append(vertice)
            elif height < min_height:
                min_height_vertices = [vertice]
                min_height = height
        
        return min_height_vertices

# timelimit exceeded


from collections import deque
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
            
        heights = {}
        adj = [[] for _ in range(n)]
        indegrees = [0] * n

        for (a, b) in edges:
            adj[a].append(b)
            adj[b].append(a)
            indegrees[a] += 1
            indegrees[b] += 1
        
        queue = deque(i for i in range(n) if indegrees[i] == 1) # not 0 but 1 as all are connected
        res = []

        while queue:
            sub_queue = deque()
            res = list(queue)

            while queue:
                vertice = queue.popleft()
                for neighbor in adj[vertice]:
                    indegrees[neighbor] -= 1
                    if indegrees[neighbor] == 1: # not 0 but 1
                        sub_queue.append(neighbor)
            
            queue = sub_queue
        
        return res
