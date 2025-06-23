from collections import deque
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if s == goal:
            return True
        
        queue_s = deque(s)
        queue_goal = deque(goal)
        start = 0
        while (idx := goal.find(s[0], start)) != -1:
            queue_s.rotate(idx)
            if queue_s == queue_goal:
                return True
            queue_s.rotate(-idx)
            start = idx + 1
        
        return False


class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        
        return goal in s+s