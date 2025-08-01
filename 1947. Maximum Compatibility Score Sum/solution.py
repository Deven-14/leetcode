class Solution:
    def maxCompatibilitySum(self, students: List[List[int]], mentors: List[List[int]]) -> int:
        n = len(students)
        m = len(students[0])

        comp_scores = [[0] * n for _ in range(n)]

        for i in range(n):
            for j in range(n):
                comp_scores[i][j] = sum(not (students[i][k] ^ mentors[j][k]) for k in range(m))
        
        max_score = 0
        visited = [False] * n
        def backtrack(i):
            if i == n:
                return 0
            
            max_score = 0
            for j in range(n):
                if not visited[j]:
                    visited[j] = True
                    max_sub_score = backtrack(i + 1)
                    max_score = max(max_score, comp_scores[i][j] + max_sub_score)
                    visited[j] = False
            
            return max_score
        
        return backtrack(0)


class Solution:
    def maxCompatibilitySum(self, students: List[List[int]], mentors: List[List[int]]) -> int:
        n = len(students)
        m = len(students[0])

        comp_scores = [[0] * n for _ in range(n)]

        for i in range(n):
            for j in range(n):
                comp_scores[i][j] = sum(students[i][k] == mentors[j][k] for k in range(m))
        
        max_score = 0
        visited = [False] * n
        def backtrack(i):
            if i == n:
                return 0
            
            max_score = 0
            for j in range(n):
                if not visited[j]:
                    visited[j] = True
                    max_sub_score = backtrack(i + 1)
                    max_score = max(max_score, comp_scores[i][j] + max_sub_score)
                    visited[j] = False
            
            return max_score
        
        return backtrack(0)


from itertools import permutations
class Solution:
    def maxCompatibilitySum(self, students: List[List[int]], mentors: List[List[int]]) -> int:
        n = len(students)
        m = len(students[0])

        comp_scores = [[0] * n for _ in range(n)]

        for i in range(n):
            for j in range(n):
                comp_scores[i][j] = sum(students[i][k] == mentors[j][k] for k in range(m))
        
        max_score = 0
        for permutation in permutations(range(n)):
            score = sum(comp_scores[i][permutation[i]] for i in range(n))
            max_score = max(score, max_score)
        
        return max_score


# ! best solution is using the KM Algorithm (Hungarian Algorithm) — Optimal for Bipartite Matching