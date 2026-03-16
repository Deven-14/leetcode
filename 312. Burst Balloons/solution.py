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


