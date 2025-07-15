class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:

        @cache
        def helper(total, choosed_integers):
            if total <= 0: # total is already reached by opponent, so I lose
                return False

            for j in range(1, maxChoosableInteger + 1):
                # if j integer is available to pick and my opponent can't win after I picked, then I win
                if ((choosed_integers & (1 << j)) == 0) and not helper(total - j, choosed_integers | (1 << j)): 
                    return True
            
            return False
        
        total = (maxChoosableInteger * (maxChoosableInteger + 1)) // 2

        if desiredTotal < 2:
            return True

        if total < desiredTotal: # no one can win
            return False

        return helper(desiredTotal, 0)


class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:

        @cache
        def helper(total, choosed_integers):
            if total <= 0: # total is already reached by opponent, so I lose
                return False

            for j in range(1, maxChoosableInteger + 1):
                # if j integer is available to pick and my opponent can't win after I picked, then I win
                curr_bit = 1 << j
                if ((choosed_integers & curr_bit) == 0) and not helper(total - j, choosed_integers | curr_bit): 
                    return True
            
            return False
        
        total = (maxChoosableInteger * (maxChoosableInteger + 1)) // 2

        if desiredTotal < 2:
            return True

        if total < desiredTotal: # no one can win
            return False

        return helper(desiredTotal, 0)



class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        cache = {}

        def helper(total, choosed_integers):
            if choosed_integers in cache:
                return cache[choosed_integers]
            
            if total <= 0: # total is already reached by opponent, so I lose
                return False

            for j in range(1, maxChoosableInteger + 1):
                # if j integer is available to pick and my opponent can't win after I picked, then I win
                curr_bit = 1 << j
                if ((choosed_integers & curr_bit) == 0) and not helper(total - j, choosed_integers | curr_bit): 
                    cache[choosed_integers] = True
                    return True
            
            cache[choosed_integers] = False
            return False
        
        total = (maxChoosableInteger * (maxChoosableInteger + 1)) // 2

        if desiredTotal < 2:
            return True

        if total < desiredTotal: # no one can win
            return False

        return helper(desiredTotal, 0)

# So memoizing with just choosed_integers is sufficient and optimal. Including T would be not just redundant, but technically incorrect — because the two parameters would not be independent.
# total = desiredTotal - sum_of_selected_numbers(choosed_integers)