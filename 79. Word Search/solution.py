class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        len_word = len(word)
        visited = [[False] * n for _ in range(m)]

        def backtrack(i, j, word_idx = 0):
            if word_idx == len_word:
                return True
            
            if i >= 0 and i < m and j >= 0 and j < n and board[i][j] == word[word_idx] and visited[i][j] == False:
                visited[i][j] = True
                for a, b in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                    if backtrack(a, b, word_idx+1):
                        return True
                visited[i][j] = False

            return False

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if backtrack(i, j):
                        return True
        
        return False


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        len_word = len(word)
        visited = [[False] * n for _ in range(m)]

        def backtrack(i, j, word_idx = 0):
            if word_idx == len_word:
                return True
            
            if i >= 0 and i < m and j >= 0 and j < n and board[i][j] == word[word_idx] and visited[i][j] == False:
                visited[i][j] = True
                word_idx = word_idx+1
                if backtrack(i-1, j, word_idx) or backtrack(i+1, j, word_idx) or backtrack(i, j-1, word_idx) or backtrack(i, j+1, word_idx):
                        return True
                visited[i][j] = False

            return False

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if backtrack(i, j):
                        return True
        
        return False
