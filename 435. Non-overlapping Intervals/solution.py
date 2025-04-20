class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        count = 0

        prev_end = intervals[0][1]
        for i in range(1, len(intervals)):
            if prev_end > intervals[i][0]:
                count += 1
            else:
                prev_end = intervals[i][1]
        
        return count


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        count = 0

        prev_end = intervals[0][1]
        for i in range(1, len(intervals)):
            start, end = intervals[i]
            if prev_end > start:
                count += 1
            else:
                prev_end = end
        
        return count


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        count = 0

        prev_end = float("-inf")
        for start, end in intervals:
            if prev_end > start:
                count += 1
            else:
                prev_end = end
        
        return count


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        count = 1

        prev_end = intervals[0][1]
        for start, end in intervals:
            if start >= prev_end:
                count += 1
                prev_end = end
        
        return len(intervals) - count
    

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        count = 0

        prev_end = intervals[0][0]
        for start, end in intervals:
            if prev_end > start:
                count += 1
            else:
                prev_end = end
        
        return count