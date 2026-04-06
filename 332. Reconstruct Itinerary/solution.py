from collections import defaultdict
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        for src, dest in tickets:
            adj[src].append(dest)
        
        for key in adj:
            adj[key].sort(reverse=True)
                
        order = []
        def dfs(src):
            while adj[src]:
                dest = adj[src].pop()
                dfs(dest)
            order.append(src)
                
        
        dfs("JFK")
        return order[::-1]


