import random
class RandomizedSet:

    def __init__(self):
        self.indexes = {}
        self.nums = []

    def insert(self, val: int) -> bool:
        if val in self.indexes:
            return False
        
        self.indexes[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.indexes:
            return False

        if len(self.nums) > 1:        
            index = self.indexes[val]
            self.nums[index], self.nums[-1] = self.nums[-1], self.nums[index]
            self.indexes[self.nums[index]] = index
        
        self.nums.pop()
        del self.indexes[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.nums)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()



import random
class RandomizedSet:

    def __init__(self):
        self.indexes = {}
        self.nums = []

    def insert(self, val: int) -> bool:
        if val in self.indexes:
            return False
        
        self.indexes[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.indexes:
            return False

        index = self.indexes[val]
        self.nums[index], self.nums[-1] = self.nums[-1], self.nums[index]
        self.indexes[self.nums[index]] = index
        
        self.nums.pop()
        del self.indexes[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.nums)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()