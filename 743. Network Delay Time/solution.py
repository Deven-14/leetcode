from collections import defaultdict, deque
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list) # or defaultdict(dict)
        for u, v, w in times:
            adj[u].append((v, w))
        
        min_times = [float('inf')] * (n + 1)
        queue = deque([k])
        in_queue = [False] * (n + 1)
        min_times[k] = 0
        in_queue[k] = True

        while queue:
            u = queue.popleft()
            in_queue[u] = False

            for v, adj_time in adj[u]:
                if (time := min_times[u] + adj_time) < min_times[v]:
                    min_times[v] = time
                    
                    if not in_queue[v]:
                        queue.append(v)
                        in_queue[v] = True
        
        min_times[0] = 0 # 0 node not present
        min_time = max(min_times)
        return -1 if min_time == float('inf') else min_time



from collections import defaultdict
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list) # or defaultdict(dict)
        for u, v, w in times:
            adj[u].append((v, w))
        
        min_times = [float('inf')] * (n + 1)
        min_times[k] = 0
        pq = [(k, 0)] # ! very important mistake here, distance has to be before the node

        while pq:
            u, curr_time = heapq.heappop(pq)
            if curr_time > min_times[u]:
                continue

            for v, adj_time in adj[u]:
                if (time := curr_time + adj_time) < min_times[v]:
                    min_times[v] = time
                    heapq.heappush(pq, (v, time))
        
        min_times[0] = 0 # 0 node not present
        min_time = max(min_times)
        return -1 if min_time == float('inf') else min_time


# * worst performing - because we didn't set is_updated properly
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        INF = float('inf')
        min_times = [INF] * (n + 1)
        min_times[k] = 0

        for _ in range(n-1):
            is_updated = False

            for u, v, w in times:
                if min_times[u] == INF:
                    continue
                
                min_times[v] = min(min_times[v], min_times[u] + w)
                is_updated = True
            
            if not is_updated:
                break

        min_times[0] = 0 # 0 node not present
        min_time = max(min_times)
        return -1 if min_time == float('inf') else min_time


# * better implementation of bellam ford, but still worse than dijkstra's or spfa
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        INF = float('inf')
        min_times = [INF] * (n + 1)
        min_times[k] = 0

        for _ in range(n-1):
            is_updated = False

            for u, v, w in times:
                if min_times[u] == INF:
                    continue
                
                if (t := min_times[u] + w) < min_times[v]:
                    min_times[v] = t
                    is_updated = True
            
            if not is_updated:
                break

        min_times[0] = 0 # 0 node not present
        min_time = max(min_times)
        return -1 if min_time == float('inf') else min_time



from collections import defaultdict
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list) # or defaultdict(dict)
        for u, v, w in times:
            adj[u].append((v, w))
        
        min_times = [float('inf')] * (n + 1)
        min_times[k] = 0
        pq = [(0, k)] # * this was fixed, time is before node now

        while pq:
            curr_time, u = heapq.heappop(pq)
            if curr_time > min_times[u]:
                continue

            for v, adj_time in adj[u]:
                if (time := curr_time + adj_time) < min_times[v]:
                    min_times[v] = time
                    heapq.heappush(pq, (time, v))
        
        min_times[0] = 0 # 0 node not present
        min_time = max(min_times)
        return -1 if min_time == float('inf') else min_time
    


from collections import defaultdict
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list) # or defaultdict(dict)
        for u, v, w in times:
            adj[u].append((v, w))
        
        min_times = [float('inf')] * (n + 1)
        min_times[k] = 0
        pq = [(0, k)]

        while pq:
            curr_time, u = heapq.heappop(pq)
            if curr_time > min_times[u]:
                continue

            for v, adj_time in adj[u]:
                if (time := curr_time + adj_time) < min_times[v]:
                    min_times[v] = time
                    heapq.heappush(pq, (time, v))
        
        min_time = max(min_times[1:])
        return -1 if min_time == float('inf') else min_time
    

    