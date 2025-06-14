class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for operation in operations:
            match operation:
                case 'C':
                    stack.pop()
                case 'D':
                    stack.append(2 * stack[-1])
                case '+':
                    stack.append(stack[-1] + stack[-2])
                case _:
                    stack.append(int(operation))
        
        return sum(stack)