from collections import Counter
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return [ele for ele, count in (Counter(nums1) & Counter(nums2)).items() for _ in range(count)]