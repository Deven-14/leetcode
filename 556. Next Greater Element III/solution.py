from bisect import bisect_right
class Solution:
    def nextGreaterElement(self, n: int) -> int:
        str_num = list(str(n))
        l = len(str_num)
        stack = [str_num.pop()]

        while str_num and str_num[-1] >= stack[-1]:
            stack.append(str_num.pop())
        
        if len(str_num) == 0:
            return -1
        
        idx = bisect_right(stack, str_num[-1])
        min_greater_digit = stack[idx]
        stack[idx] = str_num.pop()
        stack.sort()

        next_num = "".join(str_num) + min_greater_digit + "".join(stack)
        INT_MAX = str(2 ** 31 - 1)
        next_num = next_num.zfill(len(INT_MAX))
        return int(next_num) if next_num <= INT_MAX else -1

        