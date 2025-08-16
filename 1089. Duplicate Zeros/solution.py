class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        zero_count = 0
        i, n = 0, len(arr)

        while i < n:
            if arr[i] == 0:
                n -= 1
                zero_count += 1
            i += 1
            
        if i == len(arr):
            return

        if i > n:
            arr[-1] = 0
            l = len(arr) - 2
        else:
            l = len(arr) - 1
        
        j = n-1
        while j >= 0:
            arr[j], arr[l] = arr[l], arr[j]
            if arr[l] == 0:
                l -= 1
                arr[l] = 0
            j -= 1
            l -= 1

