from functools import cache
class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        
        def helper(num1, num2, remaining_num):
            total = str(num1 + num2)
            n = len(total)

            if remaining_num.startswith(total):
                if remaining_num == total:
                    return True
                if helper(num2, int(total), remaining_num[n:]):
                    return True
            
            return False

        m = len(num)
        for i in range(1, m//2+1):
            num1 = num[:i]
            if num1 != "0" and num1[0] == "0":
                return False
            
            for j in range(i+1, i+(m-i)//2+1):
                num2 = num[i:j]
                if num2 != "0" and num2[0] == "0":
                    break
                
                remaining_num = num[j:]
                if helper(int(num1), int(num2), remaining_num):
                    return True
        
        return False
                