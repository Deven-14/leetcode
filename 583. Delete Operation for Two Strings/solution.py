
# ! 80%
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        l1, l2 = len(word1) + 1, len(word2) + 1
        dp = [[0] * l1 for _ in range(l2)]

        for i in range(1, l1):
            dp[0][i] = i
        
        for j in range(1, l2):
            dp[j][0] = j
        
        for i in range(1, l2):
            for j in range(1, l1):
                if word1[j-1] == word2[i-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(dp[i][j-1], dp[i-1][j])
        
        return dp[l2-1][l1-1]

# ! 93.89%
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        l1, l2 = len(word1) + 1, len(word2) + 1
        dp = list(range(l1))
        
        for i in range(1, l2):
            prev = dp[:]
            dp[0] = i
            for j in range(1, l1):
                if word1[j-1] == word2[i - 1]:
                    dp[j] = prev[j-1]
                else:
                    dp[j] = 1 + min(dp[j-1], dp[j])
        
        return dp[l1-1]

# ! almost same as above or lesser
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        l1, l2 = len(word1) + 1, len(word2) + 1
        dp = list(range(l1))
        
        for i in range(1, l2):
            prev = dp[0]
            dp[0] = i
            for j in range(1, l1):
                curr = dp[j]
                if word1[j-1] == word2[i - 1]:
                    dp[j] = prev
                else:
                    dp[j] = 1 + min(dp[j-1], dp[j])
                prev = curr
        
        return dp[l1-1]


# * 97.72
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        l1, l2 = len(word1) + 1, len(word2) + 1
        dp = [0] * l1
        
        for i in range(1, l2):
            prev = dp[:]
            for j in range(1, l1):
                if word1[j-1] == word2[i - 1]:
                    dp[j] = prev[j-1] + 1
                else:
                    dp[j] = max(dp[j-1], dp[j])
        
        return len(word1) + len(word2) - 2 * dp[l1-1]


# ! less than above
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        l1, l2 = len(word1) + 1, len(word2) + 1
        dp = [0] * l1
        
        for i in range(1, l2):
            prev_diag = dp[0]
            for j in range(1, l1):
                curr_diag = dp[j]
                if word1[j-1] == word2[i - 1]:
                    dp[j] = prev_diag + 1
                else:
                    dp[j] = max(dp[j-1], dp[j])
                prev_diag = curr_diag
                
        return len(word1) + len(word2) - 2 * dp[l1-1]
    