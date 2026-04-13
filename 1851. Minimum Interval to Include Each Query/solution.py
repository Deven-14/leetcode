import heapq
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        i, n = 0, len(intervals)
        min_heap = []
        min_intervals = {}

        for q in sorted(queries):
            if q in min_intervals:
                continue

            while i < n and intervals[i][0] <= q:
                heapq.heappush(min_heap, (intervals[i][1] - intervals[i][0] + 1, intervals[i][0], intervals[i][1]))
                i += 1
            
            while min_heap and not (min_heap[0][1] <= q <= min_heap[0][2]):
                heapq.heappop(min_heap)
            
            min_intervals[q] = -1 if not min_heap else min_heap[0][0]
        
        return [min_intervals[q] for q in queries]


import heapq
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        i, n = 0, len(intervals)
        min_heap = []
        min_intervals = {}

        for q in sorted(set(queries)):
            
            while i < n and intervals[i][0] <= q:
                heapq.heappush(min_heap, (intervals[i][1] - intervals[i][0] + 1, intervals[i][0], intervals[i][1]))
                i += 1
            
            while min_heap and not (min_heap[0][1] <= q <= min_heap[0][2]):
                heapq.heappop(min_heap)
            
            min_intervals[q] = -1 if not min_heap else min_heap[0][0]
        
        return [min_intervals[q] for q in queries]


import heapq
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        i, n = 0, len(intervals)
        min_heap = []
        min_intervals = {}

        for q in sorted(set(queries)):
            
            while i < n and intervals[i][0] <= q:
                heapq.heappush(min_heap, (intervals[i][1] - intervals[i][0] + 1, intervals[i][1]))
                i += 1
            
            while min_heap and (min_heap[0][1] < q):
                heapq.heappop(min_heap)
            
            min_intervals[q] = -1 if not min_heap else min_heap[0][0]
        
        return [min_intervals[q] for q in queries]


