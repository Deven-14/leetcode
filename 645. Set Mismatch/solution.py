class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums_set = set()
        duplicate_num = None

        for num in nums:
            if num in nums_set:
                duplicate_num = num
            nums_set.add(num)
        
        n = len(nums)
        sum_of_n = (n * (n+1)) // 2
        sum_of_nums = sum(nums)

        return [duplicate_num, duplicate_num + (sum_of_n - sum_of_nums)]
        

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n, s1, s2 = len(nums), sum(nums), sum(set(nums))
        s3 = (n * (n+1)) // 2
        return [s1 - s2, s3 - s2]