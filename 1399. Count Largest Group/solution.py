class Solution:
    def countLargestGroup(self, n: int) -> int:
        groups = Counter(sum(int(x) for x in str(num)) for num in range(1, n + 1))
        largest_group_size = 0
        count = 0
        for group_size in groups.values():
            if group_size > largest_group_size:
                largest_group_size = group_size
                count = 1
            elif group_size == largest_group_size:
                count += 1
        return count
    

class Solution:
    def countLargestGroup(self, n: int) -> int:
        groups = [0] * 37
        largest_group_size = 0

        for num in range(1, n + 1):
            sum_of_digits = sum(int(x) for x in str(num))
            groups[sum_of_digits] += 1
            largest_group_size = max(largest_group_size, groups[sum_of_digits])

        return sum(1 for group_size in groups if group_size == largest_group_size)
    

class Solution:
    def countLargestGroup(self, n: int) -> int:
        groups = [0] * 37
        largest_group_size = 0

        for num in range(1, n + 1):
            sum_of_digits = sum(int(x) for x in str(num))
            groups[sum_of_digits] += 1
            largest_group_size = max(largest_group_size, groups[sum_of_digits])

        return sum(group_size == largest_group_size for group_size in groups)


class Solution:
    def countLargestGroup(self, n: int) -> int:
        groups = [0] * 37

        for num in range(1, n + 1):
            sum_of_digits = sum(int(x) for x in str(num))
            groups[sum_of_digits] += 1

        largest_group_size = max(groups)

        return sum(group_size == largest_group_size for group_size in groups)


class Solution:
    def countLargestGroup(self, n: int) -> int:
        dp = [0] * (n + 1) # for faster sum of digits
        groups = [0] * 37

        for num in range(1, n + 1):
            dp[num] = dp[num // 10] + (num % 10) # sum of digits of num
            groups[dp[num]] += 1

        largest_group_size = max(groups)

        return sum(group_size == largest_group_size for group_size in groups)
    

    