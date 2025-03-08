class Solution:
    def generate_parenthesis(self, n: int):
        if n == 1:
            return ["()"]
        
        parenthesis_list = self.generate_parenthesis(n-1)
        new_parenthesis_list = set()
        for parenthesis_combination in parenthesis_list:
            parenthesis = "()"
            for i in range(len(parenthesis_combination)+1):
                new_parenthesis = "".join([parenthesis_combination[:i], parenthesis, parenthesis_combination[i:]])
                new_parenthesis_list.add(new_parenthesis)

        return new_parenthesis_list


    def generateParenthesis(self, n: int) -> List[str]:
        return self.generate_parenthesis(n)


class Solution:
    def generate_parenthesis(self, n: int):
        if n == 1:
            return ["()"]
        
        parenthesis_list = self.generate_parenthesis(n-1)
        new_parenthesis_list = set()
        for parenthesis_combination in parenthesis_list:
            parenthesis = "()"
            for i in range(len(parenthesis_combination)+1):
                new_parenthesis = "".join([parenthesis_combination[:i], parenthesis, parenthesis_combination[i:]])
                new_parenthesis_list.add(new_parenthesis)

        return new_parenthesis_list


    def generateParenthesis(self, n: int) -> List[str]:
        return self.generate_parenthesis(n)


class Solution:
    def generate_parenthesis_backtrack(self, n: int, output: list, left: int = 0, right: int = 0, s: str = ""):
        if n*2 == len(s):
            output.append(s)
            return
        
        if left < n:
            self.generate_parenthesis_backtrack(n, output, left+1, right, s + '(')

        if right < left:
            self.generate_parenthesis_backtrack(n, output, left, right+1, s + ')')

    def generateParenthesis(self, n: int) -> List[str]:
        output = []
        self.generate_parenthesis_backtrack(n, output)
        return output

# 0 ms
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        parenthesis = []
        stack = []

        def backtrack(n_open = 0, n_closed = 0):
            if n_open == n_closed == n:
                parenthesis.append("".join(stack))
                return
            
            if n_open < n:
                stack.append("(")
                backtrack(n_open + 1, n_closed)
                stack.pop()
            
            if n_closed < n_open:
                stack.append(")")
                backtrack(n_open, n_closed + 1)
                stack.pop()
        
        backtrack()
        return parenthesis