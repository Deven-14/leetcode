class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        self_dividing_nums = []
        for num in range(left, right+1):
            
            digit = num
            t = num
            while t and digit != 0 and num % digit == 0:
                digit = t % 10
                t //= 10 
                
            if t == 0 and digit != 0 and num % digit == 0:
                self_dividing_nums.append(num)
        
        return self_dividing_nums