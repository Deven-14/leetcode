from functools import cache

class Solution:
    def numTrees(self, n: int) -> int:
        
        @cache
        def numTreesHelper(start, end):
            c = 0
            for root_val in range(start, end):
                c += numTreesHelper(start, root_val) * numTreesHelper(root_val+1, end)
            return c or 1
        
        return numTreesHelper(1, n+1)


# solution explanation
# https://leetcode.com/problems/unique-binary-search-trees/solutions/31666/dp-solution-in-6-lines-with-explanation-f-i-n-g-i-1-g-n-i/

from functools import cache

class Solution:
    def numTrees(self, n: int) -> int:
        if n <= 1:
            return 1
        
        dp = [0] * (n+1)
        dp[0] = dp[1] = 1

        for i in range(2, n+1):
            for j in range(1, i+1):
                dp[i] += dp[j - 1] * dp[i - j]
        
        return dp[n]


# https://leetcode.com/problems/unique-binary-search-trees/solutions/5376305/catalan-number-t-c-o-n-constant-space/
# https://en.wikipedia.org/wiki/Catalan_number


from functools import cache

class Solution:
    def numTrees(self, n: int) -> int:
        if n <= 1:
            return 1
        
        catalon = 1
        for i in range(1, n+1):
            catalon = catalon * (2 * (2 * i - 1)) / (i + 1)
        
        return int(catalon)
