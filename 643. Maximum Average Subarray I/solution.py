class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum = 0
        for i in range(k):
            window_sum += nums[i]
        
        average = window_sum / k

        for i in range(k, len(nums)):
            window_sum += (nums[i] - nums[i-k])
            average = max(average, window_sum / k)
        
        return average


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum = sum(nums[:k])        
        average = window_sum / k

        for i in range(k, len(nums)):
            window_sum += (nums[i] - nums[i-k])
            average = max(average, window_sum / k)
        
        return average


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum = sum(nums[:k])        
        max_sum = window_sum

        for i in range(k, len(nums)):
            window_sum += (nums[i] - nums[i-k])
            max_sum = max(max_sum, window_sum)
        
        return max_sum / k


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum = sum(nums[:k])        
        max_sum = window_sum

        for i, j in zip(range(k, len(nums)), range(len(nums)-k)):
            window_sum += (nums[i] - nums[j])
            max_sum = max(max_sum, window_sum)
        
        return max_sum / k



class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum = sum(nums[:k])        
        max_sum = window_sum

        j = 0
        for i in range(k, len(nums)):
            window_sum += (nums[i] - nums[j])
            max_sum = max(max_sum, window_sum)
            j += 1
        
        return max_sum / k