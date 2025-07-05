class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        e, o = 0, 0
        i, n = 0, len(nums)

        while e < n and nums[e] & 1 == 1:
            e += 1
        
        while o < n and nums[o] & 1 == 0:
            o += 1
        
        even_place = True
        while i < n and e < n and o < n:
            if even_place:
                nums[i], nums[e] = nums[e], nums[i]
                e += 1

            else:
                nums[i], nums[o] = nums[o], nums[i]
                o += 1
            
            while e < n and nums[e] & 1 == 1:
                e += 1
            while o < n and nums[o] & 1 == 0:
                o += 1
            
            i += 1
            even_place = not even_place
        
        return nums


class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        e, o, n = 0, 1, len(nums)

        while e < n and o < n:
            if nums[e] & 1 == 0:
                e += 2

            elif nums[o] & 1 == 1:
                o += 2
            
            else:
                nums[e], nums[o] = nums[o], nums[e]
                e += 2
                o += 2
        
        return nums