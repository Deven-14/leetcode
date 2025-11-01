from collections import defaultdict
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        diagonals = defaultdict(list)
        m, n = len(mat), len(mat[0])

        for i in range(m):
            for j in range(n):
                diagonals[i+j].append(mat[i][j])
        
        right = True
        diagonal_order = []
        for i in range(len(diagonals)):
            diagonal_order += diagonals[i][::-1] if right else diagonals[i]
            right = not right
        
        return diagonal_order

# https://leetcode.com/problems/diagonal-traverse/description/comments/3135774/
# Hint: If you do a standard traversal of the array, you can group the elements in each diagonal by the sum of their indices.


from collections import defaultdict
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        diagonals = defaultdict(list)
        m, n = len(mat), len(mat[0])

        for i in range(m):
            for j in range(n):
                diagonals[i+j].append(mat[i][j])
        
        right = True
        diagonal_order = []
        for i in range(len(diagonals)):
            diagonal_order.extend(diagonals[i][::-1] if right else diagonals[i])
            right = not right
        
        return diagonal_order

# https://leetcode.com/problems/diagonal-traverse/description/comments/3135774/
# Hint: If you do a standard traversal of the array, you can group the elements in each diagonal by the sum of their indices.


from collections import defaultdict, deque
from itertools import chain

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        diagonals = defaultdict(deque)
        m, n = len(mat), len(mat[0])

        for i in range(m):
            row = mat[i]
            for j in range(n):
                if (t := i+j) & 1:
                    diagonals[t].append(row[j])
                else:
                    diagonals[t].appendleft(row[j])
        
        diagonal_order = list(chain.from_iterable(diagonals[i] for i in range(len(diagonals))))
        return diagonal_order

# https://leetcode.com/problems/diagonal-traverse/description/comments/3135774/
# Hint: If you do a standard traversal of the array, you can group the elements in each diagonal by the sum of their indices.


from collections import defaultdict, deque
from itertools import chain

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        diagonals = defaultdict(deque)
        m, n = len(mat), len(mat[0])

        for i in range(m):
            row = mat[i]
            for j in range(n):
                if (t := i+j) & 1:
                    diagonals[t].append(row[j])
                else:
                    diagonals[t].appendleft(row[j])
        
        diagonal_order = []
        for i in range(len(diagonals)):
            diagonal_order.extend(diagonals[i])

        return diagonal_order

# https://leetcode.com/problems/diagonal-traverse/description/comments/3135774/
# Hint: If you do a standard traversal of the array, you can group the elements in each diagonal by the sum of their indices.


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        diagonal_order = []
        m, n = len(mat), len(mat[0])
        r, c = 0, 0

        while r < m and c < n:

            # direction up
            while r >= 0 and c < n:
                diagonal_order.append(mat[r][c])
                r -= 1
                c += 1
            
            # You either go right or you go down 
            if c < n:
                r += 1 # right
            else:
                r += 2 # down
                c -= 1
            
            # direction down
            while c >= 0 and r < m:
                diagonal_order.append(mat[r][c])
                c -= 1
                r += 1
            
            # you go down or you go to the right
            if r < m:
                c += 1 # down
            else:
                r -= 1 # right
                c += 2
        
        return diagonal_order

# https://leetcode.com/problems/diagonal-traverse/description/comments/3135774/
# Hint: If you do a standard traversal of the array, you can group the elements in each diagonal by the sum of their indices.