import heapq
class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        pairs = list(zip(nums2, nums1))
        pairs.sort(reverse=True)

        heap = []
        nums1_sum = 0
        for i in range(k):
            num2, num1 = pairs[i]
            nums1_sum += num1
            heapq.heappush(heap, num1)
        
        max_score = nums1_sum * num2

        for i in range(k, len(nums2)):
            num2, num1 = pairs[i]
            nums1_sum += num1 - heapq.heapreplace(heap, num1)
            max_score = max(max_score, nums1_sum * num2)
        
        return max_score
            

import heapq
class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        pairs = list(zip(nums2, nums1))
        pairs.sort(reverse=True)

        heap = [num1 for _, num1 in pairs[:k]]
        heapq.heapify(heap)
        nums1_sum = sum(heap)
        max_score = nums1_sum * pairs[k-1][0]

        for i in range(k, len(nums2)):
            num2, num1 = pairs[i]
            nums1_sum += num1 - heapq.heapreplace(heap, num1)
            max_score = max(max_score, nums1_sum * num2)
        
        return max_score
            

