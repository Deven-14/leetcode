class Solution:
    def findLength(self, nums1: list[int], nums2: list[int]) -> int:
        n, m = len(nums1) + 1, len(nums2) + 1
        dp = [[0] * m for _ in range(n)]
        
        for i in range(1, n):
            for j in range(1, m):
                if nums1[i-1] == nums2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                
        return max(max(dp[i]) for i in range(n))