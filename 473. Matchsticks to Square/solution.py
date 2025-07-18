class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total = sum(matchsticks)
        if total % 4 != 0:
            return False
        
        side = total // 4
        if max(matchsticks) > side:
            return False

        def helper(nums, i, combs=[], nums1=[], nums2=[], sum1=0, sum2=0):
            if sum1 == sum2:
                if i == len(nums):
                    combs.append((list(nums1), list(nums2)))
                    return 
            
            if i == len(nums):
                return 
            
            nums1.append(nums[i])
            helper(nums, i+1, combs, nums1, nums2, sum1 + nums[i], sum2)
            nums1.pop()

            nums2.append(nums[i])
            helper(nums, i+1, combs, nums1, nums2, sum1, sum2 + nums[i])
            nums2.pop()
            

        def helper2(nums, i, sum1=0, sum2=0):
            if sum1 == sum2:
                if i == len(nums):
                    return True
            
            if i == len(nums):
                return False
            
            return (
                helper2(nums, i+1, sum1 + nums[i], sum2) or
                helper2(nums, i+1, sum1, sum2 + nums[i])
            )
        

        combs = []
        helper(matchsticks, 0, combs)
        
        for nums1, nums2 in combs:
            if helper2(nums1, 0) and helper2(nums2, 0):
                return True
            
        return False


class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total = sum(matchsticks)
        if total % 4 != 0:
            return False
        
        side = total // 4
        if max(matchsticks) > side:
            return False

        side2 = side * 2

        def helper(nums, i, combs=[], nums1=[], nums2=[], sum1=0, sum2=0):
            if sum1 == sum2 == side2:
                combs.append((list(nums1), list(nums2)))
                return 
            
            if i == len(nums) or sum1 > side2 or sum2 > side2:
                return 
            
            nums1.append(nums[i])
            helper(nums, i+1, combs, nums1, nums2, sum1 + nums[i], sum2)
            nums1.pop()

            nums2.append(nums[i])
            helper(nums, i+1, combs, nums1, nums2, sum1, sum2 + nums[i])
            nums2.pop()
            

        def helper2(nums, i, sum1=0, sum2=0):
            if sum1 == sum2 == side:
                return True
            
            if i == len(nums) or sum1 > side or sum2 > side:
                return False
            
            return (
                helper2(nums, i+1, sum1 + nums[i], sum2) or
                helper2(nums, i+1, sum1, sum2 + nums[i])
            )
        

        combs = []
        helper(matchsticks, 0, combs)
        
        for nums1, nums2 in combs:
            if helper2(nums1, 0) and helper2(nums2, 0):
                return True
            
        return False


class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total = sum(matchsticks)
        if total % 4 != 0:
            return False
        
        side = total // 4
        if max(matchsticks) > side:
            return False

        side2 = side * 2

        def helper(nums, i, combs=[], nums1=[], nums2=[], sum1=0, sum2=0):
            if sum1 == sum2 == side2:
                combs.append((tuple(nums1), tuple(nums2)))
                return 
            
            if i == len(nums) or sum1 > side2 or sum2 > side2:
                return 
            
            nums1.append(nums[i])
            helper(nums, i+1, combs, nums1, nums2, sum1 + nums[i], sum2)
            nums1.pop()

            nums2.append(nums[i])
            helper(nums, i+1, combs, nums1, nums2, sum1, sum2 + nums[i])
            nums2.pop()
            
        @cache
        def helper2(nums, i, sum1=0, sum2=0):
            if sum1 == sum2 == side:
                return True
            
            if i == len(nums) or sum1 > side or sum2 > side:
                return False
            
            return (
                helper2(nums, i+1, sum1 + nums[i], sum2) or
                helper2(nums, i+1, sum1, sum2 + nums[i])
            )
        

        combs = []
        helper(matchsticks, 0, combs)
        
        for nums1, nums2 in combs:
            if helper2(nums1, 0) and helper2(nums2, 0):
                return True
            
        return False
    

class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total = sum(matchsticks)
        if total % 4 != 0:
            return False
        
        side = total // 4
        if max(matchsticks) > side:
            return False

        side2 = side * 2

        def helper(nums, i, combs=[], nums1=[], nums2=[], sum1=0, sum2=0):
            if sum1 == sum2 == side2:
                combs.append((tuple(nums1), tuple(nums2)))
                return 
            
            if i == len(nums) or sum1 > side2 or sum2 > side2:
                return 
            
            nums1.append(nums[i])
            helper(nums, i+1, combs, nums1, nums2, sum1 + nums[i], sum2)
            nums1.pop()

            nums2.append(nums[i])
            helper(nums, i+1, combs, nums1, nums2, sum1, sum2 + nums[i])
            nums2.pop()
            
        @cache
        def helper2(nums, i, sum1=0, sum2=0):
            if sum1 == sum2 == side:
                return True
            
            if i == len(nums) or sum1 > side or sum2 > side:
                return False
            
            return (
                helper2(nums, i+1, sum1 + nums[i], sum2) or
                helper2(nums, i+1, sum1, sum2 + nums[i])
            )
        

        combs = []
        helper(matchsticks, 0, combs)
        
        visited = set()
        for nums1, nums2 in combs:
            if (nums1, nums2) not in visited and helper2(nums1, 0) and helper2(nums2, 0):
                return True
            visited.add((nums1, nums2))
            visited.add((nums2, nums1))
            
        return False


# ! slower

from functools import cache
class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total = sum(matchsticks)
        if total % 4 != 0:
            return False
        
        side = total // 4
        if max(matchsticks) > side:
            return False
        
        def helper(i, sum1=0, sum2=0, sum3=0, sum4=0):
            if sum1 == sum2 == sum3 == sum4 == side:
                return True
            
            if i == len(matchsticks) or sum1 > side or sum2 > side or sum3 > side or sum4 > side:
                return False
            
            return (
                helper(i+1, sum1 + matchsticks[i], sum2, sum3, sum4) or 
                (sum1 != sum2 and helper(i+1, sum1, sum2 + matchsticks[i], sum3, sum4)) or
                (sum1 != sum3 and sum2 != sum3 and helper(i+1, sum1, sum2, sum3 + matchsticks[i], sum4)) or
                (sum1 != sum4 and sum2 != sum4 and sum3 != sum4 and helper(i+1, sum1, sum2, sum3, sum4 + matchsticks[i]))
            )
        
        return helper(0)



from functools import cache
class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total = sum(matchsticks)
        if total % 4 != 0:
            return False
        
        side = total // 4
        matchsticks.sort(reverse=True)
        if max(matchsticks) > side:
            return False
        
        def helper(i, sum1=0, sum2=0, sum3=0, sum4=0):
            if sum1 == sum2 == sum3 == sum4 == side:
                return True
            
            if i == len(matchsticks) or sum1 > side or sum2 > side or sum3 > side or sum4 > side:
                return False
            
            return (
                helper(i+1, sum1 + matchsticks[i], sum2, sum3, sum4) or 
                (sum1 != sum2 and helper(i+1, sum1, sum2 + matchsticks[i], sum3, sum4)) or
                (sum1 != sum3 and sum2 != sum3 and helper(i+1, sum1, sum2, sum3 + matchsticks[i], sum4)) or
                (sum1 != sum4 and sum2 != sum4 and sum3 != sum4 and helper(i+1, sum1, sum2, sum3, sum4 + matchsticks[i]))
            )
        
        return helper(0)


# * matchsticks.sort(reverse=True)  # Place bigger sticks first for faster pruning
