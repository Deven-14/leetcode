from functools import cache
from collections import deque
class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        l = len(expression)
        nums = []
        operators = []
        
        i = 0
        while i < l:
            chars = expression[i:i+2]
            if chars.isdigit():
                nums.append(int(chars))
                i += 2
            else:
                nums.append(int(expression[i]))
                i += 1
            if i < l:
                operators.append(expression[i])
                i += 1
        
        operations = {
            '+': lambda a, b: a+b,
            '-': lambda a, b: a-b,
            '*': lambda a, b: a*b
        }
        
        def helper(nums, operators):
            if not nums:
                return []

            if not operators:
                return [nums[0]]
            
            if len(operators) == 1:
                return [operations[operators[0]](nums[0], nums[1])]

            totals = []
            for i in range(len(operators)):
                left_sub_totals = helper(nums[:i+1], operators[:i])
                right_sub_totals = helper(nums[i+1:], operators[i+1:])
                for left_sub_total in left_sub_totals:
                    for right_sub_total in right_sub_totals:
                        totals.append(operations[operators[i]](left_sub_total, right_sub_total))

            return totals

        return helper(nums, operators)

# * SPLIT ON OPERATOR AND NOT ON THE NUMBERS OR BASED ON BRACKETS