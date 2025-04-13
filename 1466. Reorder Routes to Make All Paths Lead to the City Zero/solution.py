class Solution:

    def dfs(self, node, adj, rev_adj, parent): # since there are only (n-1) edges, it is a tree and there is no cycle and visited is not required
        changes = 0
        for adj_node in adj[node]:
            if adj_node != parent:
                changes += 1 + self.dfs(adj_node, adj, rev_adj, node)
        
        for adj_node in rev_adj[node]:
            if adj_node != parent:
                changes += self.dfs(adj_node, adj, rev_adj, node)
        
        return changes
    
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        rev_adj = [[] for _ in range(n)]
        visited = set()
        visited.add(0)
        
        for u, v in connections:
            adj[u].append(v)
            rev_adj[v].append(u)
        
        changes = self.dfs(0, adj, rev_adj, None)
        
        return changes