from itertools import accumulate
import operator
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixes = list(accumulate(nums, operator.mul))
        suffixes = list(accumulate(nums[::-1], operator.mul))

        products = [suffixes[-2]]
        for i in range(1, len(nums)-1):
            products.append(prefixes[i-1] * suffixes[-i-2])
        
        products.append(prefixes[-2])

        return products


from itertools import accumulate
import operator
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixes = list(accumulate(nums, operator.mul))
        suffixes = list(accumulate(reversed(nums), operator.mul))

        products = [suffixes[-2]]
        for i in range(1, len(nums)-1):
            products.append(prefixes[i-1] * suffixes[-i-2])
        
        products.append(prefixes[-2])

        return products


from itertools import accumulate
import operator
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefixes = [0] * n
        suffixes = [0] * n
        products = [0] * n

        prefixes[0] = suffixes[-1] = 1
        for i in range(1, n):
            prefixes[i] = prefixes[i-1] * nums[i-1]
        
        for i in range(n-2, -1, -1):
            suffixes[i] = suffixes[i+1] * nums[i+1]
        
        for i in range(n):
            products[i] = prefixes[i] * suffixes[i]
        
        return products

from itertools import accumulate
import operator
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefixes = [0] * n
        products = [0] * n

        prefixes[0] = 1
        for i in range(1, n):
            prefixes[i] = prefixes[i-1] * nums[i-1]
        
        suffix = 1
        for i in range(n-1, -1, -1):
            products[i] = prefixes[i] * suffix
            suffix *= nums[i]
        
        return products
