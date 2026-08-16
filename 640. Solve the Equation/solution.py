class Solution:
    def solveEquation(self, equation: str) -> str:
        lefteq, righteq = equation.split('=')

        def compress(eq):
            xstack = []
            numstack = []

            if eq[0] != '+' and eq[0] != '-':
                eq = '+' + eq
            
            n = len(eq)
            i = 0
            while i < n:
                operator = eq[i]
                i += 1

                operand = ""
                while i < n and eq[i] not in ('+', '-', 'x'):
                    operand += eq[i]
                    i += 1
                
                if i == n or eq[i] != 'x':
                    numstack.append(int(operand) if operator == '+' else -int(operand))
                
                else:
                    operand = 1 if operand == '' else int(operand)
                    xstack.append(operand if operator == '+' else -operand)
                    i += 1
                            
            return sum(xstack), sum(numstack)
        
        leftx, leftnum = compress(lefteq)
        rightx, rightnum = compress(righteq)
        print(leftx, leftnum, rightx, rightnum)

        x = leftx - rightx
        num = leftnum - rightnum

        if x == num == 0:
            return "Infinite solutions"
        elif x == 0 and num != 0:
            return "No solution"
        
        num = abs(num // x) if num > 0 else -abs(num // x)
        return f"x={-num if x > 0 else num}"
        
