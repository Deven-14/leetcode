import heapq
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        
        max_gap = 0
        heapq.heapify(nums)
        first = heapq.heappop(nums)

        while nums:
            second = heapq.heappop(nums)
            max_gap = max(second - first, max_gap)
            first = second

        return max_gap


from functools import reduce
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        n = len(nums)
        
        def counting_sort(str_nums, index):
            output = [0] * n
            counts = [0] * 10

            significant_digits = [int(num[index]) for num in str_nums]

            for sg in significant_digits:
                counts[sg] += 1
            
            for i in range(1, 10):
                counts[i] += counts[i-1]

            for i in range(n-1, -1, -1):
                counts[significant_digits[i]] -= 1
                output[counts[significant_digits[i]]] = str_nums[i]

            return output
        
        def radix_sort(nums):
            max_ele = max(nums)
            l = len(str(max_ele))

            str_nums = []
            for num in nums:
                str_nums.append(str(num).zfill(l))
            
            for i in range(l-1, -1, -1):
                str_nums = counting_sort(str_nums, i)
            
            for i, num in enumerate(str_nums):
                nums[i] = int(num)
        
        radix_sort(nums)

        max_diff = 0
        for first, second in pairwise(nums):
            max_diff = max(max_diff, second - first)
        
        return max_diff

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        n = len(nums)
        
        def counting_sort(str_nums, index):
            output = [0] * n
            counts = [0] * 10

            significant_digits = [int(num[index]) for num in str_nums]

            for sg in significant_digits:
                counts[sg] += 1
            
            for i in range(1, 10):
                counts[i] += counts[i-1]

            for i in range(n-1, -1, -1):
                counts[significant_digits[i]] -= 1
                output[counts[significant_digits[i]]] = str_nums[i]

            return output
        
        def radix_sort(nums):
            max_ele = max(nums)
            l = len(str(max_ele))

            str_nums = []
            for num in nums:
                str_nums.append(str(num).zfill(l))
            
            for i in range(l-1, -1, -1):
                str_nums = counting_sort(str_nums, i)
            
            for i, num in enumerate(str_nums):
                nums[i] = int(num)
        
        radix_sort(nums)

        import heapq
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        
        max_gap = 0
        heapq.heapify(nums)
        first = heapq.heappop(nums)

        while nums:
            second = heapq.heappop(nums)
            max_gap = max(second - first, max_gap)
            first = second

        return max_gap


from functools import reduce
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        n = len(nums)
        
        def counting_sort(nums, exp):
            output = [0] * n
            counts = [0] * 10

            significant_digits = [(num // exp) % 10 for num in nums]

            for sg in significant_digits:
                counts[sg] += 1
            
            for i in range(1, 10):
                counts[i] += counts[i-1]

            for i in range(n-1, -1, -1):
                counts[significant_digits[i]] -= 1
                output[counts[significant_digits[i]]] = nums[i]

            return output
        
        def radix_sort(nums):
            max_ele = max(nums)
            
            exp = 1
            for i in range(len(str(max_ele))):
                nums = counting_sort(nums, exp)
                exp *= 10
            
            return nums
        
        nums = radix_sort(nums)

        max_diff = 0
        for first, second in pairwise(nums):
            max_diff = max(max_diff, second - first)
        
        return max_diff


class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums.sort()

        max_diff = 0
        for first, second in pairwise(nums):
            max_diff = max(max_diff, second - first)
        
        return max_diff


class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        max_diff = 0
        for first, second in pairwise(sorted(set(nums))):
            max_diff = max(max_diff, second - first)
        
        return max_diff

