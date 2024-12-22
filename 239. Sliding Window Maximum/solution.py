from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_queue = deque([0])
        max_sliding_window = []

        for i in range(1, k):
            while max_queue and nums[i] >= nums[max_queue[-1]]:
                max_queue.pop()
            max_queue.append(i)
        max_sliding_window.append(nums[max_queue[0]])

        for i in range(k, len(nums)):
            if max_queue[0] == i-k:
                max_queue.popleft()
            while max_queue and nums[i] >= nums[max_queue[-1]]:
                max_queue.pop()
            max_queue.append(i)
            max_sliding_window.append(nums[max_queue[0]])
        
        return max_sliding_window

