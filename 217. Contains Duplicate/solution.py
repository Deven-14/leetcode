class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        existing = set()
        for num in nums:
            if num in existing:
                return True
            existing.add(num)
        
        return False


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))