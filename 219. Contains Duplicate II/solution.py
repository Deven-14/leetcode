class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        visited = {}

        for i, num in enumerate(nums):
            if num in visited:
                if i-visited[num] <= k:
                    return True
            
            visited[num] = i
        
        return False