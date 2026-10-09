class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        n, m = len(s1) + 1, len(s2) + 1
        dp = [[0] * m for _ in range(n)]

        for i in range(1, n):
            dp[i][0] = dp[i-1][0] + ord(s1[i-1])
        
        for j in range(1, m):
            dp[0][j] = dp[0][j-1] + ord(s2[j-1])

        for i in range(1, n):
            for j in range(1, m):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(
                        dp[i-1][j] + ord(s1[i-1]),
                        dp[i][j-1] + ord(s2[j-1]),
                        dp[i-1][j-1] + ord(s1[i-1]) + ord(s2[j-1])
                    )
        
        return dp[n-1][m-1]


class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        s1 = list(ord(char) for char in s1)
        s2 = list(ord(char) for char in s2)

        n, m = len(s1) + 1, len(s2) + 1
        dp = [[0] * m for _ in range(n)]

        for i in range(1, n):
            dp[i][0] = dp[i-1][0] + s1[i-1]
        
        for j in range(1, m):
            dp[0][j] = dp[0][j-1] + s2[j-1]

        for i in range(1, n):
            for j in range(1, m):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(
                        dp[i-1][j] + s1[i-1],
                        dp[i][j-1] + s2[j-1],
                        dp[i-1][j-1] + s1[i-1] + s2[j-1]
                    )
        
        return dp[n-1][m-1]


class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        s1 = list(ord(char) for char in s1)
        s2 = list(ord(char) for char in s2)

        n, m = len(s1) + 1, len(s2) + 1
        dp = [[0] * m for _ in range(n)]

        for i in range(1, n):
            dp[i][0] = dp[i-1][0] + s1[i-1]
        
        for j in range(1, m):
            dp[0][j] = dp[0][j-1] + s2[j-1]

        for i in range(1, n):
            for j in range(1, m):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(
                        dp[i-1][j] + s1[i-1],
                        dp[i][j-1] + s2[j-1],
                    )
        
        return dp[n-1][m-1]


class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        s1 = list(ord(char) for char in s1)
        s2 = list(ord(char) for char in s2)

        n, m = len(s1) + 1, len(s2) + 1
        dp = [0] * m

        for j in range(1, m):
            dp[j] = dp[j-1] + s2[j-1]

        for i in range(1, n):
            dp1 = dp.copy()
            dp[0] += s1[i-1]

            for j in range(1, m):
                if s1[i-1] == s2[j-1]:
                    dp[j] = dp1[j-1]
                else:
                    dp[j] = min(
                        dp[j] + s1[i-1],
                        dp[j-1] + s2[j-1],
                    )
                    
        return dp[m-1]


class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        s1 = list(ord(char) for char in s1)
        s2 = list(ord(char) for char in s2)

        n, m = len(s1) + 1, len(s2) + 1
        dp = [0] * m

        for j in range(1, m):
            dp[j] = dp[j-1] + s2[j-1]

        for i in range(1, n):
            prev = dp[0]
            dp[0] += s1[i-1]

            for j in range(1, m):
                t = prev
                prev = dp[j]
                if s1[i-1] == s2[j-1]:
                    dp[j] = t
                else:
                    dp[j] = min(
                        dp[j] + s1[i-1],
                        dp[j-1] + s2[j-1],
                    )
                    
        return dp[m-1]


