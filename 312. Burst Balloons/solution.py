from functools import cache
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        
        @cache
        def postorder(l, r):
            max_coins = 0
            for i in range(l, r + 1):
                coins = nums[l - 1] * nums[i] * nums[r + 1]
                coins += postorder(l, i - 1)
                coins += postorder(i + 1, r)
                max_coins = max(max_coins, coins)
            
            return max_coins
        
        return postorder(1, len(nums)-2)


from functools import cache
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        
        @cache
        def postorder(l, r):
            max_coins = 0
            boundary_product = nums[l - 1] * nums[r + 1]
            for i in range(l, r + 1):
                coins =  nums[i] * boundary_product
                coins += postorder(l, i - 1)
                coins += postorder(i + 1, r)
                max_coins = max(max_coins, coins)
            
            return max_coins
        
        return postorder(1, len(nums)-2)


from functools import cache
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        
        @cache
        def postorder(l, r):
            if l > r:
                return 0
            
            max_coins = 0
            boundary_product = nums[l - 1] * nums[r + 1]
            for i in range(l, r + 1):
                coins =  nums[i] * boundary_product
                coins += postorder(l, i - 1)
                coins += postorder(i + 1, r)
                max_coins = max(max_coins, coins)
            
            return max_coins
        
        return postorder(1, len(nums)-2)


from functools import cache
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        
        @cache
        def postorder(l, r):
            if l > r:
                return 0
            
            max_coins = 0
            boundary_product = nums[l] * nums[r]
            for i in range(l + 1, r):
                coins =  nums[i] * boundary_product
                coins += postorder(l, i)
                coins += postorder(i, r)
                max_coins = max(max_coins, coins)
            
            return max_coins
        
        return postorder(0, len(nums)-1)
    


from functools import cache
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        m = len(nums)
        dp = [[0] * m for _ in range(m)]
        
        for l in range(m - 1, -1, -1):
            for r in range(l + 1, m):

                boundary_product = nums[l] * nums[r]
                for i in range(l + 1, r):
                    coins =  nums[i] * boundary_product + dp[l][i] + dp[i][r]
                    dp[l][r] = max(dp[l][r], coins)

        return dp[0][m-1]




from functools import cache
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        m = len(nums)
        dp = [[0] * m for _ in range(m)]
        
        for l in range(m - 2, -1, -1):
            for r in range(l + 2, m):

                boundary_product = nums[l] * nums[r]
                for i in range(l + 1, r):
                    coins =  nums[i] * boundary_product + dp[l][i] + dp[i][r]
                    dp[l][r] = max(dp[l][r], coins)

        return dp[0][m-1]


# Why delta = 2, i.e, l + 2 is the starting point

# If delta = 1:

# That means r = l + 1
# There are no balloons between l and r
# So dp[l][r] = 0 (already initialized)
# No computation needed.




from functools import cache
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [num for num in nums if num > 0]
        nums = [1] + nums + [1]
        m = len(nums)
        dp = [[0] * m for _ in range(m)]
        
        for l in range(m - 2, -1, -1):
            for r in range(l + 2, m):

                boundary_product = nums[l] * nums[r]
                for i in range(l + 1, r):
                    coins =  nums[i] * boundary_product + dp[l][i] + dp[i][r]
                    dp[l][r] = max(dp[l][r], coins)

        return dp[0][m-1]


# Why delta = 2, i.e, l + 2 is the starting point

# If delta = 1:

# That means r = l + 1
# There are no balloons between l and r
# So dp[l][r] = 0 (already initialized)
# No computation needed.

