from collections import deque
class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        queue = deque(nums)
        n = len(nums)

        max_value = sum(i * num for i, num in enumerate(nums))
        total = sum(nums)
        prev = max_value
        for i in range(1, len(nums)):
            queue.rotate(1)
            value = prev + total - queue[0] * n # n coz 1 for total, and n-1 is the actual last
            max_value = max(max_value, value)
            prev = value
        
        return max_value

class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        max_value = sum(i * num for i, num in enumerate(nums))
        total = sum(nums)
        prev = max_value
        
        for i in range(len(nums) - 1, 0, -1):
            value = prev + total - nums[i] * n # n coz 1 for total, and n-1 is the actual last
            max_value = max(max_value, value)
            prev = value
        
        return max_value


class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        value = sum(i * num for i, num in enumerate(nums))
        total = sum(nums)
        prev = value
        values = [value]

        for i in range(n - 1, 0, -1):
            value = prev + total - nums[i] * n # n coz 1 for total, and n-1 is the actual last
            values.append(value)
            prev = value
        
        return max(values)

class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        value = sum(i * num for i, num in enumerate(nums))
        total = sum(nums)
        values = [value]

        for i in range(n - 1, 0, -1):
            value += total - nums[i] * n # n coz 1 for total, and n-1 is the actual last
            values.append(value)
        
        return max(values)

class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        value = sum(i * num for i, num in enumerate(nums))
        total = sum(nums)
        max_value = value

        for i in range(n - 1, 0, -1):
            value += total - nums[i] * n # n coz 1 for total, and n-1 is the actual last
            if value > max_value:
                max_value = value
        
        return max_value
