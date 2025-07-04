import bisect
class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        indexes = { start: i for i, (start, _) in enumerate(intervals) }
        starts = list(indexes.keys())
        ends = list(end for _, end in intervals)
        starts.sort()

        right_intervals = []
        n = len(intervals)
        for end in ends:
            j = bisect_right(starts, end)
            if j-1 >= 0 and starts[j-1] == end:
                j = j-1
            right_intervals.append(indexes[starts[j]] if j != n else -1)
        
        return right_intervals
        

import bisect
class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        indexes = { start: i for i, (start, _) in enumerate(intervals) }
        indexes[float("inf")] = -1
        starts = list(indexes.keys())
        starts.append(float("inf"))
        ends = list(end for _, end in intervals)
        starts.sort()

        right_intervals = [indexes[starts[bisect_left(starts, end)]] for end in ends]
        return right_intervals
        