class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:

        @cache
        def helper(i, j):
            if i > j:
                return 0

            if i == j:
                return 1

            if s[i] == s[j]:
                return 2 + helper(i + 1, j - 1)

            return max(helper(i + 1, j), helper(i, j - 1))
        
        return helper(0, len(s) - 1)
    

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            dp[i][i] = 1 # single char

            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[i][j] = 2 + dp[i + 1][j - 1]
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        
        return dp[0][n - 1]


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [0] * n

        for i in range(n - 1, -1, -1):
            dp[i] = 1 # single char
            prev_diag = 0

            for j in range(i + 1, n):
                temp = dp[j]
                if s[i] == s[j]:
                    dp[j] = 2 + prev_diag
                else:
                    dp[j] = max(dp[j], dp[j - 1]) # max(down, left) - max(dp[i+1][j], dp[i][j-1])
                prev_diag = temp
        
        return dp[n - 1]


