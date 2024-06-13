class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        overlapping_intervals = []

        current = intervals[0]
        for interval in intervals[1:]:
            if current[1] >= interval[0]:
                current = [current[0], max(current[1], interval[1])]
            else:
                overlapping_intervals.append(current)
                current = interval
        
        overlapping_intervals.append(current)

        return overlapping_intervals