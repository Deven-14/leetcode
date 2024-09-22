class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        l = n-k
        if k == 0:
            return
        
        to_be_moved = nums[-k:]
        nums[-l:] = nums[:l]
        nums[:k] = to_be_moved[:]