class Solution:
    def minOperations(self, logs: List[str]) -> int:
        level = 0

        for log in logs:
            match log:
                case "../":
                    level = max(0, level - 1)
                case "./":
                    pass
                case _:
                    level += 1
        
        return level
        