class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        stack = [-1]
        for i in range(len(arr)-1, 0, -1):
            stack.append(arr[i] if arr[i] > stack[-1] else stack[-1])
        stack.reverse()
        return stack


from collections import deque
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        queue = deque([-1])
        for i in range(len(arr)-1, 0, -1):
            queue.appendleft(arr[i] if arr[i] > queue[0] else queue[0])
        return list(queue)