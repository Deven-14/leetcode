class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        m = n // 4

        i = 0
        while i < n:
            j = i + 1
            c = 0
            while j < n and arr[i] == arr[j]:
                c += 1
                j += 1
            
            if c >= m:
                return arr[i]

            i = j
        


class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        m = n // 4

        i = 0
        while i < n:
            if arr[i] == arr[i + m]:
                return arr[i]
            
            j = i + 1
            while arr[j] == arr[i]:
                j += 1
            i = j
        