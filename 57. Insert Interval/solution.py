class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]
        
        i = 0
        n = len(intervals)
        new_intervals = []

        start, end = newInterval
        while i < n and intervals[i][1] < start:
            new_intervals.append(intervals[i])
            i += 1

        if i == 0 and end < intervals[0][0]:
            new_intervals.append(newInterval)
            new_intervals.extend(intervals)
            return new_intervals
        
        if i == n:
            new_intervals.append(newInterval)
            return new_intervals
        
        start = min(intervals[i][0], start)
        
        while i < n and end >= intervals[i][0]:
            i += 1
        
        end = max(intervals[i-1][1], end)
        new_intervals.append([start, end])
        new_intervals.extend(intervals[i:])

        return new_intervals

