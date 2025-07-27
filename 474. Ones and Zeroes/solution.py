from functools import cache
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        counts0 = [string.count('0') for string in strs]
        counts1 = [string.count('1') for string in strs]

        filtered_counts0 = []
        filtered_counts1 = []
        for count0, count1 in zip(counts0, counts1):
            if count0 <= m and count1 <= n:
                filtered_counts0.append(count0)
                filtered_counts1.append(count1)

        l = len(filtered_counts0)
        
        @cache
        def helper(i, c0, c1):
            if c0 > m or c1 > n:
                return -1
            
            if i == l:
                return 0

            return max(
                1 + helper(i+1, c0 + filtered_counts0[i], c1 + filtered_counts1[i]),
                helper(i+1, c0, c1)
            )
        
        return helper(0, 0, 0)
        
