from heapq import nsmallest
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        return list(nsmallest(k, points, key=lambda x: x[0] * x[0] + x[1] * x[1]))


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        return sorted(points, key=lambda x: x[0] * x[0] + x[1] * x[1])[:k]
    
