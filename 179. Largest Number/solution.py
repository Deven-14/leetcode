class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        str_nums = [str(num) for num in nums]

        class cmp:
            def __init__(self, obj):
                self.obj = obj
            
            def __lt__(self, other):
                return int(self.obj + other.obj) < int(other.obj + self.obj)

        str_nums.sort(key=cmp, reverse=True)
        return str(int("".join(str_nums)))


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        str_nums = [str(num) for num in nums]

        class cmp:
            def __init__(self, obj):
                self.obj = obj
            
            def __lt__(self, other):
                return int(self.obj + other.obj) < int(other.obj + self.obj)

        str_nums.sort(key=cmp, reverse=True)
        
        if str_nums[0] == "0":
            return "0"

        return "".join(str_nums)