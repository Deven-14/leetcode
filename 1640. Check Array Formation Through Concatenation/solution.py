class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        starts = { piece[0]: piece for piece in pieces }

        i, n = 0, len(arr)
        while i < n:
            if arr[i] not in starts:
                return False
            
            for num in starts[arr[i]]:
                if num != arr[i]:
                    return False
                i += 1
        
        return True