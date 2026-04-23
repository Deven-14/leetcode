
# ! Time Limit Exceeded

from itertools import accumulate
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if len(nums) == 1:
            return False
        
        prefix_sum = list(accumulate(nums, initial=0))

        for i in range(2, len(prefix_sum)):
            for j in range(i - 1): # [0, i-1) => [0, i-2]
                diff = prefix_sum[i] - prefix_sum[j]
                if diff == 0 or diff % k == 0:
                    return True
        
        return False


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        visited = { 0: -1 } # for case subarry starting from index 0
        curr_sum = 0

        for i, num in enumerate(nums):
            curr_sum = (curr_sum + num) % k

            if curr_sum in visited:
                if i - visited[curr_sum] > 1:
                    return True
            else: # important, to save only first occurrence
                visited[curr_sum] = i
        
        return False


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        visited = { 0: -1 } # for case subarry starting from index 0
        curr_sum = 0

        for i, num in enumerate(nums):
            curr_sum = (curr_sum + num) % k

            if curr_sum in visited:
                if i - visited[curr_sum] > 1:
                    return True
            else: # important, to save only first occurrence
                visited[curr_sum] = i
        
        return False


# https://leetcode.com/problems/continuous-subarray-sum/description/comments/1564916/

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        visited = set()
        curr_sum = 0
        prev = 0

        for num in nums:
            curr_sum = (curr_sum + num) % k

            if curr_sum in visited:
                return True

            visited.add(prev)
            prev = curr_sum
        
        return False


# https://leetcode.com/problems/continuous-subarray-sum/description/comments/1564916/