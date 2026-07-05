class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        arr = [0] * (2 * n)
        arr[::2] = nums[:n]
        arr[1::2] = nums[n:]
        return arr


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        arr = []
        for i in range(n):
            arr.append(nums[i])
            arr.append(nums[n + i])
        return arr



class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        arr = [0] * (2 * n)
        arr[::2] = nums[:n]
        arr[1::2] = nums[n:]
        return arr



