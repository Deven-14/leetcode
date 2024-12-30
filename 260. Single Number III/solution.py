class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        visited = set()
        for num in nums:
            if num not in visited:
                visited.add(num)
            else:
                visited.remove(num)
        
        return list(visited)