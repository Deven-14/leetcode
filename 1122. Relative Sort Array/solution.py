class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr2_indices = { num: idx for idx, num in enumerate(arr2) }
        max_num = max(arr2)
        arr1.sort(key=lambda num: arr2_indices.get(num, num + max_num))
        return arr1