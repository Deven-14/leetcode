
# * Upper Bound
# * (arr[:l] <= target, arr[l:] > target), arr[:l] - so l is one greater
# * bisect.bisect_right(nums, target)

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) # * NO -1, important coz l can be len(nums) as well, because l can be one greater for arr[:l]

        while l < r:
            m = l + ((r - l) // 2)  
            if nums[m] > target:
                r = m
            elif nums[m] <= target:
                l = m + 1                      # * (arr[:l] <= target, arr[l:] > target), arr[:l] - so l is one greater
        return l - 1 if (l and nums[l - 1] == target) else -1

# * for upper bound, "=" should go to the "l" as upper bound should give the element greater than target
# * so all "less than or equal to" will go to left
# * VISE-VERSA for "lower bound"




# * Lower Bound
# * (arr[:l] < target, arr[l:] >= target), arr[:l] - so l is one greater
# * bisect.bisect_left(nums, target)

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) # * NO -1, important coz l can be len(nums) as well, because l can be one greater for arr[:l]

        while l < r:
            m = l + ((r - l) // 2)  
            if nums[m] >= target:
                r = m
            elif nums[m] < target:
                l = m + 1                     # * (arr[:l] < target, arr[l:] >= target), arr[:l] - so l is one greater
        return l if (l < len(nums) and nums[l] == target) else -1


# eg. [1, 2, 3, 4, 4, 4, 4, 5, 6, 7, 8]
# target = 4

# * using lower bound we get index 3
# * using upper bound we get index 7

# you can also use bisect_left and bisect_right from the bisect module