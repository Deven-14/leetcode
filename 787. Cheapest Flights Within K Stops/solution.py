from collections import deque
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = [[] for _ in range(n)]
        for u, v, price in flights:
            adj[u].append((v, price))
        
        min_prices = [float('inf')] * n
        queue = deque([(0, src, 0)])
        min_prices[src] = 0

        while queue:
            curr_price, u, stops = queue.popleft()
            if stops > k:
                continue
            
            for v, to_price in adj[u]:
                if (price := curr_price + to_price) < min_prices[v]:
                    min_prices[v] = price
                    queue.append((price, v, stops + 1))
                    
        return -1 if min_prices[dst] == float('inf') else min_prices[dst]


# * go through all posibilities for stops <= k
# * and then at last return the min_prices[dst]
# * don't check if u == dst and don't return the
# * first reachable one with min heap