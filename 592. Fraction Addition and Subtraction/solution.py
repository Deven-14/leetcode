from math import gcd
class Solution:
    def extract_fractions(self, expression):
        fractions = []

        n = len(expression)
        i = 0 
        while i < n:
            j = i + 1
            while j < n and expression[j] != '+' and expression[j] != '-':
                j += 1
            x, y = expression[i:j].split('/')
            fractions.append((int(x), int(y)))
            i = j
        
        return fractions
    
    def calculate(self, fractions):
        fx, fy = fractions[0]
        for i in range(1, len(fractions)):
            sx, sy = fractions[i]
            fx = fx * sy + sx * fy
            fy *= sy

        divisor = gcd(abs(fx), fy)
        return fx // divisor, fy // divisor

    def fractionAddition(self, expression: str) -> str:
        fractions = self.extract_fractions(expression)
        fx, fy = self.calculate(fractions)
        return f"{fx}/{fy}"
        

