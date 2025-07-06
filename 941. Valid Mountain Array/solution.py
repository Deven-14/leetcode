class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        
        i, n = 1, len(arr)
        while i < n and arr[i-1] < arr[i]:
            i += 1
        
        if i == n or i == 1:
            return False

        while i < n and arr[i-1] > arr[i]:
            i += 1
        
        return i == n