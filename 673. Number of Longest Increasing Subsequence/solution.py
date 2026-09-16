class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        
        @cache
        def dfs(i, prev):
            if i == n:
                return 0, 1

            l1, c1 = 0, 0
            if nums[i] > prev:
                l1, c1 = dfs(i + 1, nums[i])
                l1 += 1
                
            l2, c2 = dfs(i + 1, prev)
            
            if l1 > l2:
                return (l1, c1)
            elif l2 > l1:
                return (l2, c2)
            
            return (l1, c1 + c2)
        
        l, c = dfs(0, float("-inf"))
        return c


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        
        @cache
        def dfs(i):
            length = 1
            count = 1

            for j in range(i):
                if nums[j] < nums[i]:
                    prev_length, prev_count = dfs(j)

                    if (l := prev_length + 1) > length:
                        length = l
                        count = prev_count
                    
                    elif l == length:
                        count += prev_count
                
            return length, count
        

        rl, rc = 0, 0
        for i in range(len(nums)):
            l, c = dfs(i)

            if l > rl:
                rl = l
                rc = c
            elif l == rl:
                rc += c
        
        return rc