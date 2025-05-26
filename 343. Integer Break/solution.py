class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0] * (n+1)
        dp[0] = 0
        dp[1] = 1
        dp[2] = 1
        
        for i in range(3, n+1):
            l, r = 1, i-1
            
            while l <= r:
                dp[i] = max(dp[i], max(l, dp[l]) * max(r, dp[r]))
                l += 1
                r -= 1
        
        return dp[n]


class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        
        if n == 3:
            return 2
        
        dp = [0] * (n+1)
        dp[0] = 0
        dp[1] = 1
        dp[2] = 2
        dp[3] = 3
        
        for i in range(3, n+1):
            l, r = 1, i-1
            
            while l <= r:
                dp[i] = max(dp[i], dp[l] * dp[r])
                l += 1
                r -= 1
        
        return dp[n]


class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        
        if n == 3:
            return 2
        
        m, r = divmod(n, 3)
        if r == 1: # r == 1, means n == 4, x*3*1 (3 + 1) < x*4
            m -= 1
            r += 3

        product = 3 ** m
        product *= (r or 1)
        return product