import re
class Solution:
    def calculate(self, s: str) -> int:
        operations = {
            '+': lambda a, b: a+b, 
            '-': lambda a, b: a-b, 
            '*': lambda a, b: a*b, 
            '/': lambda a, b: int(a/b)
        }
        precedences = {
            '+': 0, 
            '-': 0, 
            '*': 1, 
            '/': 1
        }
        operators = {'+', '-', '*', '/'}
        opt_stack = []
        val_stack = []

        for char in re.split(r"(\b\d+)", s):
            if char.isdigit():
                val_stack.append(int(char))
            elif (operator:=char.strip()) in operators:
                while opt_stack and precedences[opt_stack[-1]] >= precedences[operator]:
                    operation = operations[opt_stack[-1]]
                    operand2, operand1 = val_stack.pop(), val_stack.pop()
                    val_stack.append(operation(operand1, operand2))
                    opt_stack.pop()
                    
                opt_stack.append(operator)
        
        while opt_stack:
            operation = operations[opt_stack[-1]]
            operand2, operand1 = val_stack.pop(), val_stack.pop()
            val_stack.append(operation(operand1, operand2))
            opt_stack.pop()
        
        return val_stack[0]


import re
class Solution:
    def calculate(self, s: str) -> int:
        operations = {
            '+': lambda a, b: a+b, 
            '-': lambda a, b: a-b, 
            '*': lambda a, b: a*b, 
            '/': lambda a, b: int(a/b)
        }
        precedences = {
            '+': 0, 
            '-': 0, 
            '*': 1, 
            '/': 1
        }
        operators = {'+', '-', '*', '/'}
        opt_stack = []
        val_stack = []

        for char in re.split(r"(\d+)", s):
            char = char.strip()
            if char.isdigit():
                val_stack.append(int(char))
            elif char in operators:
                while opt_stack and precedences[opt_stack[-1]] >= precedences[char]:
                    operation = operations[opt_stack[-1]]
                    operand2, operand1 = val_stack.pop(), val_stack.pop()
                    val_stack.append(operation(operand1, operand2))
                    opt_stack.pop()
                    
                opt_stack.append(char)
        
        while opt_stack:
            operation = operations[opt_stack[-1]]
            operand2, operand1 = val_stack.pop(), val_stack.pop()
            val_stack.append(operation(operand1, operand2))
            opt_stack.pop()
        
        return val_stack[0]


from itertools import groupby
class Solution:
    def calculate(self, s: str) -> int:
        operations = {
            '+': lambda a, b: a+b, 
            '-': lambda a, b: a-b, 
            '*': lambda a, b: a*b, 
            '/': lambda a, b: int(a/b)
        }
        precedences = {
            '+': 0, 
            '-': 0, 
            '*': 1, 
            '/': 1
        }
        operators = {'+', '-', '*', '/'}
        opt_stack = []
        val_stack = []

        for is_digit, group in groupby(s.replace(" ", ""), lambda char: char.isdigit()):
            char = "".join(group)
            if is_digit:
                val_stack.append(int(char))
            else:
                while opt_stack and precedences[opt_stack[-1]] >= precedences[char]:
                    operation = operations[opt_stack[-1]]
                    operand2, operand1 = val_stack.pop(), val_stack.pop()
                    val_stack.append(operation(operand1, operand2))
                    opt_stack.pop()
                    
                opt_stack.append(char)
        
        while opt_stack:
            operation = operations[opt_stack[-1]]
            operand2, operand1 = val_stack.pop(), val_stack.pop()
            val_stack.append(operation(operand1, operand2))
            opt_stack.pop()
        
        return val_stack[0]


from itertools import groupby
class Solution:
    def calculate(self, s: str) -> int:
        operations = {
            '+': lambda a, b: a+b, 
            '-': lambda a, b: a-b, 
            '*': lambda a, b: a*b, 
            '/': lambda a, b: int(a/b)
        }
        precedences = {
            '+': 0, 
            '-': 0, 
            '*': 1, 
            '/': 1
        }
        operators = {'+', '-', '*', '/'}
        opt_stack = []
        val_stack = []

        for char in re.split(r"(\d+)", s.replace(" ", "")):
            if char.isdigit():
                val_stack.append(int(char))
            elif char in operators:
                while opt_stack and precedences[opt_stack[-1]] >= precedences[char]:
                    operation = operations[opt_stack[-1]]
                    operand2, operand1 = val_stack.pop(), val_stack.pop()
                    val_stack.append(operation(operand1, operand2))
                    opt_stack.pop()
                    
                opt_stack.append(char)
        
        while opt_stack:
            operation = operations[opt_stack[-1]]
            operand2, operand1 = val_stack.pop(), val_stack.pop()
            val_stack.append(operation(operand1, operand2))
            opt_stack.pop()
        
        return val_stack[0]

from itertools import groupby
class Solution:
    def calculate(self, s: str) -> int:
        operations = {
            '+': lambda a, b: a+b, 
            '-': lambda a, b: a-b, 
            '*': lambda a, b: a*b, 
            '/': lambda a, b: int(a/b)
        }
        precedences = {
            '+': 0, 
            '-': 0, 
            '*': 1, 
            '/': 1
        }
        operators = {'+', '-', '*', '/'}
        opt_stack = []
        val_stack = []

        for char in re.split(r"(\+|-|\*|/)", s.replace(" ", "")):
            if char.isdigit():
                val_stack.append(int(char))
            elif char in operators:
                while opt_stack and precedences[opt_stack[-1]] >= precedences[char]:
                    operation = operations[opt_stack[-1]]
                    operand2, operand1 = val_stack.pop(), val_stack.pop()
                    val_stack.append(operation(operand1, operand2))
                    opt_stack.pop()
                    
                opt_stack.append(char)
        
        while opt_stack:
            operation = operations[opt_stack[-1]]
            operand2, operand1 = val_stack.pop(), val_stack.pop()
            val_stack.append(operation(operand1, operand2))
            opt_stack.pop()
        
        return val_stack[0]


from itertools import groupby
class Solution:
    def calculate(self, s: str) -> int:
        def operation(operator, a, b):
            if operator == '+':
                return a+b
            elif operator == '-':
                return a-b
            elif operator == '*':
                return a*b
            else:
                return int(a/b)
        
        precedences = {
            '+': 0, 
            '-': 0, 
            '*': 1, 
            '/': 1
        }
        operators = {'+', '-', '*', '/'}
        opt_stack = []
        val_stack = []

        for char in re.split(r"(\+|-|\*|/)", s.replace(" ", "")):
            if char.isdigit():
                val_stack.append(int(char))
            elif char in operators:
                while opt_stack and precedences[opt_stack[-1]] >= precedences[char]:
                    operand2, operand1 = val_stack.pop(), val_stack.pop()
                    val_stack.append(operation(opt_stack.pop(), operand1, operand2))
                    
                opt_stack.append(char)
        
        while opt_stack:
            operand2, operand1 = val_stack.pop(), val_stack.pop()
            val_stack.append(operation(opt_stack.pop(), operand1, operand2))
        
        return val_stack[0]


from itertools import groupby
class Solution:
    def calculate(self, s: str) -> int:
        def operation(operator, a, b):
            if operator == '+':
                return a+b
            elif operator == '-':
                return a-b
            elif operator == '*':
                return a*b
            else:
                return int(a/b)
        
        precedences = {
            '+': 0, 
            '-': 0, 
            '*': 1, 
            '/': 1
        }
        opt_stack = []
        val_stack = []

        for char in re.split(r"(\+|-|\*|/)", s.replace(" ", "")):
            if char.isdigit():
                val_stack.append(int(char))
            elif char in "+-*/":
                while opt_stack and precedences[opt_stack[-1]] >= precedences[char]:
                    operand2, operand1 = val_stack.pop(), val_stack.pop()
                    val_stack.append(operation(opt_stack.pop(), operand1, operand2))
                    
                opt_stack.append(char)
        
        while opt_stack:
            operand2, operand1 = val_stack.pop(), val_stack.pop()
            val_stack.append(operation(opt_stack.pop(), operand1, operand2))
        
        return val_stack[0]


from itertools import groupby
class Solution:
    def calculate(self, s: str) -> int:
        def operation(operator, a, b):
            if operator == '+':
                return a+b
            elif operator == '-':
                return a-b
            elif operator == '*':
                return a*b
            else:
                return int(a/b)

        precedences = {
            '+': 0, 
            '-': 0, 
            '*': 1, 
            '/': 1
        }

        opt_stack = []
        val_stack = []
        curr_num = 0

        for char in s:
            if char.isdigit():
                curr_num = 10*curr_num + int(char)
            elif char in "+-*/":
                val_stack.append(curr_num)
                while opt_stack and precedences[opt_stack[-1]] >= precedences[char]:
                    operand2, operand1 = val_stack.pop(), val_stack.pop()
                    val_stack.append(operation(opt_stack.pop(), operand1, operand2))
                    
                opt_stack.append(char)
                curr_num = 0
        
        val_stack.append(curr_num)

        while opt_stack:
            operand2, operand1 = val_stack.pop(), val_stack.pop()
            val_stack.append(operation(opt_stack.pop(), operand1, operand2))

        return val_stack[0]


from itertools import groupby
class Solution:
    def calculate(self, s: str) -> int:
        operations = {
            '+': lambda a, b: a+b, 
            '-': lambda a, b: a-b, 
            '*': lambda a, b: a*b, 
            '/': lambda a, b: int(a/b)
        }
        precedences = {
            '+': 0, 
            '-': 0, 
            '*': 1, 
            '/': 1
        }

        opt_stack = []
        val_stack = []
        curr_num = 0

        for char in s:
            if char.isdigit():
                curr_num = 10*curr_num + int(char)
            elif char in "+-*/":
                val_stack.append(curr_num)
                while opt_stack and precedences[opt_stack[-1]] >= precedences[char]:
                    operation = operations[opt_stack[-1]]
                    operand2, operand1 = val_stack.pop(), val_stack.pop()
                    val_stack.append(operation(operand1, operand2))
                    opt_stack.pop()

                opt_stack.append(char)
                curr_num = 0
        
        val_stack.append(curr_num)

        while opt_stack:
            operation = operations[opt_stack[-1]]
            operand2, operand1 = val_stack.pop(), val_stack.pop()
            val_stack.append(operation(operand1, operand2))
            opt_stack.pop()
            
        return val_stack[0]


from itertools import groupby
class Solution:
    def calculate(self, s: str) -> int:
        prev, curr, result = 0, 0, 0
        operator = '+'

        for char in s + "+":
            if char.isdigit():
                curr = 10*curr + int(char)
            elif char == " ":
                continue
            else:
                if operator == "+":
                    result += prev
                    prev = curr
                elif operator == "-":
                    result += prev
                    prev = -curr
                elif operator == "*":
                    prev *= curr
                else:
                    prev = int(prev/curr)
                
                curr = 0
                operator = char
        
        return result + prev


from itertools import groupby
class Solution:
    def calculate(self, s: str) -> int:
        prev, curr, result = 0, 0, 0
        operator = '+'

        s = s.replace(" ", "") + "+"
        for char in s:
            if char.isdigit():
                curr = 10*curr + int(char)
            else:
                if operator == "+":
                    result += prev
                    prev = curr
                elif operator == "-":
                    result += prev
                    prev = -curr
                elif operator == "*":
                    prev *= curr
                else:
                    prev = int(prev/curr)
                
                curr = 0
                operator = char
        
        return result + prev