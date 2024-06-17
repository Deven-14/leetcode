class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1) + 1
        m = len(word2) + 1

        grid = [[0] * n for _ in range(m)]

        grid[0] = list(range(n))
        
        for i in range(m):
            grid[i][0] = i
        
        for i in range(1, m):
            for j in range(1, n):
                if word1[j-1] == word2[i-1]:
                    grid[i][j] = grid[i-1][j-1]
                else:
                    grid[i][j] = min(grid[i-1][j-1], grid[i-1][j], grid[i][j-1]) + 1
        
        return grid[m-1][n-1]


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1) + 1
        m = len(word2) + 1

        grid = [[0] * n for _ in range(m)]

        grid[0] = list(range(n))
        
        for i in range(m):
            grid[i][0] = i
        
        for i in range(1, m):
            i_1 = i-1
            char = word2[i_1]
            for j in range(1, n):
                j_1 = j-1
                if word1[j_1] == char:
                    grid[i][j] = grid[i_1][j_1]
                else:
                    grid[i][j] = min(grid[i_1][j_1], grid[i_1][j], grid[i][j_1]) + 1
        
        return grid[m-1][n-1]