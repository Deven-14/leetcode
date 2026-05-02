from itertools import pairwise
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        timePoints.sort()
        day_minutes = 1440 # minutes
        min_diff = float('inf')
        for a, b in pairwise(timePoints):
            t1 = int(a[:2]) * 60 + int(a[3:])
            t2 = int(b[:2]) * 60 + int(b[3:])
            min_diff = min(min_diff, t2 - t1, (t1 - t2 + day_minutes) % day_minutes)
        
        if len(timePoints) > 2:
            a = timePoints[0]
            b = timePoints[-1]
            t1 = int(a[:2]) * 60 + int(a[3:])
            t2 = int(b[:2]) * 60 + int(b[3:])
            min_diff = min(min_diff, (t1 - t2 + day_minutes) % day_minutes)
        
        return min_diff


from itertools import pairwise
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        timePoints = [int(t[:2]) * 60 + int(t[3:]) for t in timePoints]
        timePoints.sort()
        day_minutes = 1440 # minutes
        min_diff = float('inf')
        for t1, t2 in pairwise(timePoints):
            min_diff = min(min_diff, t2 - t1, (t1 - t2 + day_minutes) % day_minutes)
        
        if len(timePoints) > 2:
            t1 = timePoints[0]
            t2 = timePoints[-1]
            min_diff = min(min_diff, (t1 - t2 + day_minutes) % day_minutes)
        
        return min_diff
    

from itertools import pairwise
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        timePoints = [int(t[:2]) * 60 + int(t[3:]) for t in timePoints]
        timePoints.sort()
        day_minutes = 1440 # minutes
        min_diff = day_minutes
        for t1, t2 in pairwise(timePoints):
            min_diff = min(min_diff, t2 - t1)
        
        t1 = timePoints[0]
        t2 = timePoints[-1]
        min_diff = min(min_diff, (t1 - t2 + day_minutes) % day_minutes)
        
        return min_diff


from itertools import pairwise
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        timePoints = sorted(int(t[:2]) * 60 + int(t[3:]) for t in timePoints)
        day_minutes = 1440 # minutes
        min_diff = day_minutes
        for t1, t2 in pairwise(timePoints):
            min_diff = min(min_diff, t2 - t1)
            if min_diff == 0:
                return 0
        
        t1 = timePoints[0]
        t2 = timePoints[-1]
        min_diff = min(min_diff, (t1 - t2 + day_minutes) % day_minutes)
        
        return min_diff