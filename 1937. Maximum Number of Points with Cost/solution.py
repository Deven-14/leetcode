from functools import cache
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        ROWS = len(points)
        COLS = len(points[0])
        
        @cache
        def dfs(curr_row, prev_col, curr_points):
            if curr_row == ROWS:
                return curr_points
            
            max_total = 0
            for c in range(COLS):
                new_total = dfs(curr_row + 1, c, curr_points + points[curr_row][c] - abs(prev_col - c))
                max_total = max(max_total, new_total)
            
            return max_total
        
        max_total = 0
        for c in range(COLS):
            total = dfs(1, c, points[0][c])
            max_total = max(max_total, total)
        
        return max_total

# ! Time Limit Exceeded

from functools import cache
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        ROWS = len(points)
        COLS = len(points[0])
        
        @cache
        def dfs(curr_row, prev_col):
            if curr_row == ROWS:
                return 0
            
            max_total = 0
            for c in range(COLS):
                curr_points = dfs(curr_row + 1, c)
                max_total = max(max_total, curr_points + points[curr_row][c] - abs(prev_col - c))
            
            return max_total
        
        max_total = 0
        for c in range(COLS):
            total = dfs(1, c)
            max_total = max(max_total, total + points[0][c])
        
        return max_total

# ! Time Limit Exceeded

from functools import cache
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        ROWS = len(points)
        COLS = len(points[0])
        
        dp = [[0] * COLS for _ in range(ROWS)]

        dp[0] = points[0].copy()

        for i in range(1, ROWS):
            for j in range(COLS):
                for k in range(COLS):
                    dp[i][j] = max(
                            dp[i][j], 
                            dp[i-1][k] + points[i][j] - abs(j - k)
                        )
        
        return max(dp[-1])


# ! Time Limit Exceeded

from functools import cache
class Solution:

    def cal_left_max(self, dp, row, COLS):
        left_max = []
        max_idx = 0
        left_max.append(dp[row][0])

        for i in range(1, COLS):
            t = dp[row][max_idx] - (i - max_idx)
            if dp[row][i] >= t:
                max_idx = i
                left_max.append(dp[row][i])
            else:
                left_max.append(t)
        
        return left_max    
    
    def cal_right_max(self, dp, row, COLS):
        right_max = [0] * COLS
        max_idx = COLS-1
        right_max[COLS-1] = dp[row][max_idx]

        for i in range(COLS-2, -1, -1):
            t = dp[row][max_idx] - (max_idx - i)
            if dp[row][i] >= t:
                max_idx = i
                right_max[i] = dp[row][i]
            else:
                right_max[i] = t
        
        return right_max

    def maxPoints(self, points: List[List[int]]) -> int:
        ROWS = len(points)
        COLS = len(points[0])
        
        dp = [[0] * COLS for _ in range(ROWS)]

        dp[0] = points[0].copy()

        for i in range(1, ROWS):
            left_max = self.cal_left_max(dp, i-1, COLS)
            right_max = self.cal_right_max(dp, i-1, COLS)

            for j in range(COLS):
                dp[i][j] = max(
                    dp[i][j], 
                    left_max[j] + points[i][j],
                    right_max[j] + points[i][j]
                )

        return max(dp[-1])


# * 75 %

from functools import cache
class Solution:

    def cal_left_max(self, dp, row, COLS):
        left_max = []
        max_idx = 0
        left_max.append(dp[row][0])

        for i in range(1, COLS):
            t = dp[row][max_idx] - (i - max_idx)
            if dp[row][i] >= t:
                max_idx = i
                left_max.append(dp[row][i])
            else:
                left_max.append(t)
        
        return left_max    
    
    def cal_right_max(self, dp, row, COLS):
        right_max = [0] * COLS
        max_idx = COLS-1
        right_max[COLS-1] = dp[row][max_idx]

        for i in range(COLS-2, -1, -1):
            t = dp[row][max_idx] - (max_idx - i)
            if dp[row][i] >= t:
                max_idx = i
                right_max[i] = dp[row][i]
            else:
                right_max[i] = t
        
        return right_max

    def maxPoints(self, points: List[List[int]]) -> int:
        ROWS = len(points)
        COLS = len(points[0])
        
        dp = [[0] * COLS for _ in range(ROWS)]

        dp[0] = points[0].copy()

        for i in range(1, ROWS):
            left_max = self.cal_left_max(dp, i-1, COLS)
            right_max = self.cal_right_max(dp, i-1, COLS)

            for j in range(COLS):
                dp[i][j] = points[i][j] + max(left_max[j], right_max[j])

        return max(dp[-1])

# * 84%

from functools import cache
class Solution:

    def cal_left_max(self, dp):
        left_max = []
        max_idx = 0
        left_max.append(dp[0])

        for i in range(1, len(dp)):
            t = dp[max_idx] - (i - max_idx)
            if dp[i] >= t:
                max_idx = i
                left_max.append(dp[i])
            else:
                left_max.append(t)
        
        return left_max    
    
    def cal_right_max(self, dp):
        COLS = len(dp)
        right_max = [0] * COLS
        max_idx = COLS-1
        right_max[COLS-1] = dp[max_idx]

        for i in range(COLS-2, -1, -1):
            t = dp[max_idx] - (max_idx - i)
            if dp[i] >= t:
                max_idx = i
                right_max[i] = dp[i]
            else:
                right_max[i] = t
        
        return right_max

    def maxPoints(self, points: List[List[int]]) -> int:
        ROWS = len(points)
        COLS = len(points[0])
        
        dp = points[0].copy()

        for i in range(1, ROWS):
            left_max = self.cal_left_max(dp)
            right_max = self.cal_right_max(dp)

            for j in range(COLS):
                dp[j] = points[i][j] + max(left_max[j], right_max[j])

        return max(dp)


# * 94%


from functools import cache
class Solution:

    def cal_left_max(self, dp):
        left_max = [0] * len(dp)
        left_max[0] = dp[0]

        for i in range(1, len(dp)):
            left_max[i] = max(dp[i], left_max[i-1] - 1)
        
        return left_max    
    
    def cal_right_max(self, dp):
        COLS = len(dp)
        right_max = [0] * COLS
        right_max[COLS-1] = dp[COLS - 1]

        for i in range(COLS-2, -1, -1):
            right_max[i] = max(dp[i], right_max[i+1] - 1)
        
        return right_max

    def maxPoints(self, points: List[List[int]]) -> int:
        ROWS = len(points)
        COLS = len(points[0])
        
        dp = points[0].copy()

        for i in range(1, ROWS):
            left_max = self.cal_left_max(dp)
            right_max = self.cal_right_max(dp)

            for j in range(COLS):
                dp[j] = points[i][j] + max(left_max[j], right_max[j])

        return max(dp)


class Solution:

    def cal_left_max(self, dp, left_max):
        left_max[0] = dp[0]

        for i in range(1, len(dp)):
            left_max[i] = max(dp[i], left_max[i-1] - 1)
            
    
    def cal_right_max(self, dp, right_max):
        COLS = len(dp)
        right_max[COLS-1] = dp[COLS - 1]

        for i in range(COLS-2, -1, -1):
            right_max[i] = max(dp[i], right_max[i+1] - 1)
        

    def maxPoints(self, points: List[List[int]]) -> int:
        ROWS = len(points)
        COLS = len(points[0])
        
        dp = points[0].copy()
        left_max = [0] * COLS
        right_max = [0] * COLS

        for i in range(1, ROWS):
            self.cal_left_max(dp, left_max)
            self.cal_right_max(dp, right_max)

            for j in range(COLS):
                dp[j] = points[i][j] + max(left_max[j], right_max[j])

        return max(dp)

