class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        n = len(arr)

        if arr[0] > k:
            return k

        i, j = 1, n - 1
        res = n
        while i <= j:
            mid = (i + j) // 2
            diff = arr[mid] - (mid + 1)

            if diff < k:
                i = mid + 1
            else:
                res = mid
                j = mid - 1
        
        return arr[res - 1] + (k - (arr[res - 1] - res))


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        n = len(arr)
        i, j = 0, n - 1

        while i <= j:
            mid = (i + j) // 2
            diff = arr[mid] - (mid + 1)

            if diff < k:
                i = mid + 1
            else:
                j = mid - 1
        
        return i + k

