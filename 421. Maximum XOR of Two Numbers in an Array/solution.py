class Node:
    def __init__(self):
        self.bit0 = None
        self.bit1 = None    

class NumTrie:
    def __init__(self, max_num):
        self.head = Node()
        self.length = len(f"{max_num:b}")
        self.format = f"0{self.length}b"
    
    def insert(self, num):
        node = self.head
        for bit in f"{num:{self.format}}":
            if bit == '0':
                if not node.bit0:
                    node.bit0 = Node()
                node = node.bit0
            else:
                if not node.bit1:
                    node.bit1 = Node()
                node = node.bit1
            
    def max_xor(self, num):
        node = self.head
        new_num = []
        
        for bit in f"{num:{self.format}}":
            if bit == '0' and node.bit1:
                new_num.append('1')
                node = node.bit1
            
            elif bit == '1' and node.bit0:
                new_num.append('1')
                node = node.bit0

            else:
                node = node.bit0 or node.bit1
                new_num.append('0')
        
        return int("".join(new_num), 2)

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        num_trie = NumTrie(max(nums))

        for num in nums:
            num_trie.insert(num)
        
        max_xor = 0
        for num in nums:
            max_xor = max(max_xor, num_trie.max_xor(num))
        
        return max_xor


# ! 50%
class Node:
    def __init__(self):
        self.bit0 = None
        self.bit1 = None    

class NumTrie:
    def __init__(self, max_num):
        self.head = Node()
        self.length = len(f"{max_num:b}")
        self.format = f"0{self.length}b"
    
    def insert(self, num):
        node = self.head
        for bit in f"{num:{self.format}}":
            if bit == '0':
                if not node.bit0:
                    node.bit0 = Node()
                node = node.bit0
            else:
                if not node.bit1:
                    node.bit1 = Node()
                node = node.bit1
            
    def max_xor(self, num):
        node = self.head
        new_num = [None] * self.length
        
        for i, bit in enumerate(f"{num:{self.format}}"):
            if bit == '0' and node.bit1:
                new_num[i] = '1'
                node = node.bit1
            
            elif bit == '1' and node.bit0:
                new_num[i] = '1'
                node = node.bit0

            else:
                node = node.bit0 or node.bit1
                new_num[i] = '0'
        
        return int("".join(new_num), 2)

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        num_trie = NumTrie(max(nums))

        for num in nums:
            num_trie.insert(num)
        
        max_xor = 0
        for num in nums:
            max_xor = max(max_xor, num_trie.max_xor(num))
        
        return max_xor



# ! slower 34%

class Node:
    def __init__(self):
        self.bit0 = None
        self.bit1 = None

class NumTrie:
    def __init__(self):
        self.head = Node()
    
    def insert(self, num):
        bitIndex = 30 # 0-30 (31)
        node = self.head

        while bitIndex >= 0:
            mask = 1 << bitIndex
            bit = 1 if (mask & num) > 0 else 0

            if bit == 0:
                if not node.bit0:
                    node.bit0 = Node()
                node = node.bit0
            else:
                if not node.bit1:
                    node.bit1 = Node()
                node = node.bit1
            
            bitIndex -= 1
                    
    def max_xor(self, num):
        node = self.head
        xor_num = 0
        bitIndex = 30
        
        while bitIndex >= 0:
            mask = 1 << bitIndex
            bit = 1 if (mask & num) > 0 else 0

            if bit == 0 and node.bit1:
                xor_num |= mask
                node = node.bit1
            
            elif bit == 1 and node.bit0:
                xor_num |= mask
                node = node.bit0

            else:
                node = node.bit0 or node.bit1
            
            bitIndex -= 1
        
        return xor_num

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        num_trie = NumTrie()

        for num in nums:
            num_trie.insert(num)
        
        max_xor = 0
        for num in nums:
            max_xor = max(max_xor, num_trie.max_xor(num))
        
        return max_xor


class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        max_xor = 0
        mask = 0

        for i in range(31, -1, -1):

            mask |= (1 << i) # 100...00, 110...000, 1110...00,... 111...111
            prefix_set = set(num & mask for num in nums) # prefix
            greedy_try = max_xor | (1 << i)

            for prefix in prefix_set:
                other_num = prefix ^ greedy_try # a ^ b = c === a ^ c = b
                if other_num in prefix_set:
                    max_xor = greedy_try
                    break
        
        return max_xor


import math
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        max_xor = 0
        mask = 0

        max_num = max(nums)
        if max_num == 0:
            return 0
        bits = int(math.log2(max(nums)))
        for i in range(bits, -1, -1):

            mask |= (1 << i) # 100...00, 110...000, 1110...00,... 111...111
            prefix_set = set(num & mask for num in nums) # prefix
            greedy_try = max_xor | (1 << i)

            for prefix in prefix_set:
                other_num = prefix ^ greedy_try # a ^ b = c === a ^ c = b
                if other_num in prefix_set:
                    max_xor = greedy_try
                    break
        
        return max_xor


import math
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        max_xor = 0
        mask = 0

        max_num = max(nums)
        if max_num == 0:
            return 0
        bits = int(math.log2(max(nums)))
        for i in range(bits, -1, -1):

            mask |= (1 << i) # 100...00, 110...000, 1110...00,... 111...111
            prefix_set = set() # prefix
            greedy_try = max_xor | (1 << i)

            for num in nums:
                prefix = num & mask
                other_num = prefix ^ greedy_try # a ^ b = c === a ^ c = b
                if other_num in prefix_set:
                    max_xor = greedy_try
                    break
                else:
                    prefix_set.add(prefix)
        
        return max_xor

