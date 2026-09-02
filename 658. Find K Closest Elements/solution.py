import bisect
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        idx = bisect.bisect_left(arr, x)
        i, j = idx - 1, idx
        n = len(arr)
        res = deque()

        while len(res) < k and i >= 0 and j < n:
            if abs(arr[i] - x) <= abs(arr[j] - x):
                res.appendleft(arr[i])
                i -= 1
            else:
                res.append(arr[j])
                j += 1
        
        while len(res) < k and i >= 0:
            res.appendleft(arr[i])
            i -= 1
        
        while len(res) < k and j < n:
            res.append(arr[j])
            j += 1

        return list(res)


import bisect
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, len(arr) - k
        
        while l < r:
            mid = (l + r) // 2
            if x - arr[mid] > arr[mid + k] - x:
                l = mid + 1
            else:
                r = mid
        
        return arr[l:l + k]

