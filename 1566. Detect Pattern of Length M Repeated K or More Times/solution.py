class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        n = len(arr)
        for i in range(n):
            count = 1
            l = i + m
            while l < n and arr[i:i + m] == arr[l:l + m] and count < k:
                count += 1
                l += m
            if count == k:
                return True
        
        return False
                    
class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        n = len(arr)
        count = 0
        res_count = (k - 1) * m

        for i in range(n - m):
            if arr[i] == arr[i + m]:
                count += 1
            else:
                count = 0
            if count == res_count:
                return True
        
        return False
                    
