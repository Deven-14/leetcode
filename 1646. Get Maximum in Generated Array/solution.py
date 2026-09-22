class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n < 2:
            return n
        
        dp = [0] * ((n if n & 1 == 1 else n + 1) + 1)
        dp[1] = 1
        for i in range(1, n // 2 + 1):
            dp[2 * i] = dp[i]
            dp[2 * i + 1] = dp[i] + dp[i + 1]
        
        if n & 1 == 0:
            dp.pop()

        return max(dp)


