class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:
            if not stack or (stack[-1] > 0 and asteroid > 0) or (stack[-1] < 0 and asteroid < 0):
                stack.append(asteroid)
            
            elif asteroid > 0:
                stack.append(asteroid)
            
            elif asteroid < 0:
                while stack and stack[-1] > 0 and stack[-1] < abs(asteroid):
                    stack.pop()
                
                if not stack or stack[-1] < 0:
                    stack.append(asteroid)
                elif stack[-1] + asteroid == 0:
                    stack.pop()
            
        return stack

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:
            if not stack or asteroid > 0:
                stack.append(asteroid)
            
            elif asteroid < 0:
                while stack and stack[-1] > 0 and stack[-1] < abs(asteroid):
                    stack.pop()
                
                if not stack or stack[-1] < 0:
                    stack.append(asteroid)
                elif stack[-1] + asteroid == 0:
                    stack.pop()
            
        return stack

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:
            if not stack or asteroid > 0:
                stack.append(asteroid)
            
            elif asteroid < 0:
                abs_asteroid = abs(asteroid)
                while stack and stack[-1] > 0 and stack[-1] < abs_asteroid:
                    stack.pop()
                
                if not stack or stack[-1] < 0:
                    stack.append(asteroid)
                elif stack[-1] + asteroid == 0:
                    stack.pop()
            
        return stack

