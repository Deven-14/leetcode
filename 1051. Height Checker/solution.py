class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected_heights = sorted(heights)
        n = sum(1 for i in range(len(heights)) if heights[i] != expected_heights[i])
        return n