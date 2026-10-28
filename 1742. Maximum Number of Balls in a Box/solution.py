class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        return Counter(sum(int(n) for n in str(num)) for num in range(lowLimit, highLimit + 1)).most_common(1)[0][1]


class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:

        def sum_of_digits(num):
            total = 0
            while num:
                num, digit = divmod(num, 10)
                total += digit
            return total

        return Counter(sum_of_digits(num) for num in range(lowLimit, highLimit + 1)).most_common(1)[0][1]


class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:

        def sum_of_digits(num):
            total = 0
            while num:
                num, digit = divmod(num, 10)
                total += digit
            return total

        return max(Counter(sum_of_digits(num) for num in range(lowLimit, highLimit + 1)).values())


class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        boxes = [0] * 46

        def sum_of_digits(num):
            total = 0
            while num:
                num, digit = divmod(num, 10)
                total += digit
            return total

        for num in range(lowLimit, highLimit + 1):
            boxes[sum_of_digits(num)] += 1
        return max(boxes)


class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        boxes = [0] * 46

        def sum_of_digits(num):
            total = 0
            while num:
                num, digit = divmod(num, 10)
                total += digit
            return total

        sod = sum_of_digits(lowLimit)
        boxes[sod] += 1

        for num in range(lowLimit + 1, highLimit + 1):
            if num % 10 == 0:
                sod = sum_of_digits(num)
            else:
                sod += 1
            boxes[sod] += 1
        return max(boxes)


