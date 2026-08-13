class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        n = len(price)
        m = len(special)

        def can_use_offer(offer, rem_needs):
            return all(rem_needs[j] >= offer[j] for j in range(n))
        
        @cache
        def dp(i, rem_needs):
            if i == m:
                return sum(price[j] * rem_needs[j] for j in range(n))
            
            if sum(rem_needs) == 0:
                return 0
            
            offer = special[i]
            pick = float('inf')
            if can_use_offer(offer, rem_needs):
                # pick with could pick again (i instead of (i + 1))
                rem_needs_after_pick = tuple(rem_needs[j] - offer[j] for j in range(n))
                pick = dp(i, rem_needs_after_pick) + offer[n]
            
            # not pick
            not_pick = dp(i + 1, rem_needs)

            return min(pick, not_pick)
        
        return dp(0, tuple(needs))


            
            
class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        n = len(price)
        m = len(special)

        def can_use_offer(offer, rem_needs):
            return all(rem_needs[j] >= offer[j] for j in range(n))
        
        @cache
        def dp(i, rem_needs):
            if i == m:
                return sum(price[j] * rem_needs[j] for j in range(n))
            
            offer = special[i]
            pick = float('inf')
            if can_use_offer(offer, rem_needs):
                # pick with could pick again (i instead of (i + 1))
                rem_needs_after_pick = tuple(rem_needs[j] - offer[j] for j in range(n))
                pick = dp(i, rem_needs_after_pick) + offer[n]
            
            # not pick
            not_pick = dp(i + 1, rem_needs)

            return min(pick, not_pick)
        
        return dp(0, tuple(needs))


            
            

class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        n = len(price)
        m = len(special)

        @cache
        def dp(i, req):
            if i == m:
                return sum(price[j] * req[j] for j in range(n))
            
            offer = special[i]
            pick = float('inf')

            new_req = list(req)
            for j in range(n):
                if req[j] < offer[j]:
                    break
                new_req[j] -= offer[j]
            else:
                # pick with could pick again (i instead of (i + 1))
                pick = dp(i, tuple(new_req)) + offer[n]
            
            # not pick
            not_pick = dp(i + 1, req)

            return min(pick, not_pick)
        
        return dp(0, tuple(needs))


            
class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        n = len(price)
        m = len(special)
        
        mul = lambda a, b: a * b

        @cache
        def dp(i, req):
            if i == m:
                return sum(map(mul, price, req))
            
            offer = special[i]
            pick = float('inf')

            new_req = list(req)
            for j in range(n):
                if req[j] < offer[j]:
                    break
                new_req[j] -= offer[j]
            else:
                # pick with could pick again (i instead of (i + 1))
                pick = dp(i, tuple(new_req)) + offer[n]
            
            # not pick
            not_pick = dp(i + 1, req)

            return min(pick, not_pick)
        
        return dp(0, tuple(needs))


            
            
class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        n = len(price)
        m = len(special)
        
        mul = lambda a, b: a * b

        @cache
        def backtrack(i, req):
            ans = sum(map(mul, price, req))
            
            for offer in special:

                new_req = list(req)
                for j in range(n):
                    if req[j] < offer[j]:
                        break
                    new_req[j] -= offer[j]
                else:
                    new_ans = backtrack(i, tuple(new_req)) + offer[n]
                    ans = min(ans, new_ans)
            
            return ans
        
        return backtrack(0, tuple(needs))


            
            
class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        n = len(price)
        m = len(special)
        
        mul = lambda a, b: a * b

        @cache
        def backtrack(i, req):
            ans = sum(map(mul, price, req))
            
            for offer in special:

                new_req = list(req)
                for j in range(n):
                    if req[j] < offer[j]:
                        break
                    new_req[j] -= offer[j]
                else:
                    ans = min(ans, backtrack(i, tuple(new_req)) + offer[n])
            
            return ans
        
        return backtrack(0, tuple(needs))


