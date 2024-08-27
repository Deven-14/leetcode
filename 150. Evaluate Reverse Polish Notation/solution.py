class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            match token:
                case '+':
                    second, first = stack.pop(), stack.pop()
                    stack.append(first + second)
                case '-':
                    second, first = stack.pop(), stack.pop()
                    stack.append(first - second)
                case '*':
                    second, first = stack.pop(), stack.pop()
                    stack.append(first * second)
                case '/':
                    second, first = stack.pop(), stack.pop()
                    stack.append(int(first / second))
                case _:
                    stack.append(int(token))
        
        return stack[0]
