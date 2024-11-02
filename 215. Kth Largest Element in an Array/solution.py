from heapq import nlargest
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return nlargest(k, nums)[k-1]


from heapq import heapify, heappop
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        neg_nums = [-num for num in nums]
        heapify(neg_nums)

        while k:
            num = heappop(neg_nums)
            k -= 1
        
        return -num


import random
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        def quick_select(nums, k):
            target = random.choice(nums)
            left, mid, right = [], [], []

            for num in nums:
                if num < target:
                    left.append(num)
                elif num == target:
                    mid.append(num)
                else:
                    right.append(num)
            
            if len(right) >= k:
                return quick_select(right, k)
            
            if len(right) + len(mid) < k:
                return quick_select(left, k - len(right) - len(mid))
            
            return target # in case k = len(right) + len(mid)
        
        return quick_select(nums, k)