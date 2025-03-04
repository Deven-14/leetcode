from collections import deque
class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        nodes = deque(preorder.split(","))

        def helper():
            if not nodes:
                return False

            node = nodes.popleft()
            if node == "#":
                return True
            
            return helper() and helper()
        
        return helper() and not bool(nodes)