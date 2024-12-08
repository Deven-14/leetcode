class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        m = n//3

        if n == 1:
            return [nums[0]]
        
        first, count = nums[0], 0
        for num in nums:
            if count == 0:
                first = num
                count = 1
            elif first == num:
                count += 1
            else:
                count -= 1

        if nums.count(first) <= m:
            return []
        
        second, count = nums[0], 0
        for num in nums:
            if num == first:
                continue
            
            if count == 0:
                second = num
                count = 1
            if second == num:
                count += 1
            else:
                count -= 1
        
        if second == first:
            return [first]

        if nums.count(second) > m:
            return [first, second]
        
        return [first]


# ! this above solution is wrong because in the second conidtion we are excluding the first element but in the first condition we are not excluding the second element

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        m = n//3

        if n == 1:
            return [nums[0]]
        
        first, fcount = None, 0
        second, scount = None, 0
        for num in nums:
            if fcount == 0:
                first = num
                fcount = 1
            elif first == num:
                fcount += 1
            elif scount == 0:
                second = num
                scount = 1
            elif second == num:
                scount += 1
            else:
                fcount -= 1
                scount -= 1

        total_first_count = nums.count(first)
        total_second_count = nums.count(second)

        result = []
        if total_first_count > m:
            result.append(first)
        if total_second_count > m:
            result.append(second)
        
        return result


# ! above solution is incorrect because we are not checking if the first and second are same or not, 
# ! eg: when fcount = 0 and first = 5, and scount = 0+ (eg: 3) and second = 6, 
# ! and then next iteration we get num = 6, it'll make fcount = 1 and first = 6 which is wrong

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        m = n//3

        if n == 1:
            return [nums[0]]
        
        first, fcount = None, 0
        second, scount = None, 0
        for num in nums:
            if first == num:
                fcount += 1
            elif second == num:
                scount += 1
            elif fcount == 0:
                first = num
                fcount = 1
            elif scount == 0:
                second = num
                scount = 1
            else:
                fcount -= 1
                scount -= 1

        total_first_count = nums.count(first)
        total_second_count = nums.count(second)

        result = []
        if total_first_count > m:
            result.append(first)
        if total_second_count > m:
            result.append(second)
        
        return result