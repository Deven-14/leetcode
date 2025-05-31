from functools import cache
class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        total_capacity = x + y
        seen = set()

        def dfs(total):
            if total in seen or total < 0 or total > total_capacity:
                return False
            if total == target:
                return True

            seen.add(total)
            
            return dfs(total+x) or dfs(total-x) or dfs(total+y) or dfs(total-y)
        
        return dfs(0)


from math import gcd
class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        return target <= x+y and (target % gcd(x, y) == 0)
    

# I see a lot of solutions using gcd, but no one explains why it works. So I do some research and find out that the problem is just like a implementation of a math theory named "Bezout's Lemma". I copy the definition below, and you can find the proof of it on google if you are interested in it.

# Bezout's Lemma states that if x and y are nonzero integers and g = gcd(x,y), then there exist integers a and b such that ax+by=g. In other words, there exists a linear combination of x and y equal to g.

# * https://www.youtube.com/watch?v=H64zAay5ULU&t=49s