class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        return sum(all(abs(ele2 - ele1) > d for ele2 in arr2) for ele1 in arr1)


import bisect
class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()
        n = len(arr2)
        count = 0
        
        for ele1 in arr1:
            idx = bisect.bisect_left(arr2, ele1)
            if idx > 0:
                if abs(ele1 - arr2[idx - 1]) <= d:
                    continue
            if idx < n:
                if abs(ele1 - arr2[idx]) <= d:
                    continue
            count += 1

        return count
        
