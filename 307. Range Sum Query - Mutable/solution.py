from itertools import accumulate
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.running_sum = list(accumulate(nums))
        self.running_sum.append(0)
        self.n = len(nums)

    def update(self, index: int, val: int) -> None:
        diff = val - self.nums[index] 
        self.nums[index] = val
        self.running_sum[index:-1] = [self.running_sum[i] + diff for i in range(index, self.n)]

    def sumRange(self, left: int, right: int) -> int:
        return self.running_sum[right] - self.running_sum[left-1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)

# time limit exceeded


class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class SegmentTree:
    def __init__(self, nums):
        self.n = len(nums)
        self.l = 0
        self.r = self.n-1
        self.root = self._make_tree(nums, self.l, self.r)

    def _make_tree(self, nums, l, r):
        if l == r:
            return Node(nums[l])
        
        node = Node()
        mid = (l+r) // 2
        node.left = self._make_tree(nums, l, mid)
        node.right = self._make_tree(nums, mid+1, r)
        node.val = node.left.val + node.right.val
        return node
    
    def update(self, index, val):

        def update_helper(node, l, r):
            if l == r:
                node.val = val
                return
            
            mid = (l+r) // 2
            if index <= mid:
                update_helper(node.left, l, mid)
            else:
                update_helper(node.right, mid+1, r)
            
            node.val = (node.left.val if node.left else 0) + (node.right.val if node.right else 0)
        
        update_helper(self.root, self.l, self.r)

    def sum_range(self, start, stop):
        
        def sum_range_helper(node, l, r):
            if l > stop or r < start or l > r:
                return 0
            if l >= start and r <= stop:
                return node.val

            mid = (l+r) // 2
            left_sum = sum_range_helper(node.left, l, mid)
            right_sum = sum_range_helper(node.right, mid+1, r)
            
            return left_sum + right_sum
        
        return sum_range_helper(self.root, self.l, self.r)

class NumArray:

    def __init__(self, nums: List[int]):
        self.segment_tree = SegmentTree(nums)

    def update(self, index: int, val: int) -> None:
        self.segment_tree.update(index, val)
        
    def sumRange(self, left: int, right: int) -> int:
        return self.segment_tree.sum_range(left, right)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)


class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class SegmentTree:
    def __init__(self, nums):
        self.n = len(nums)
        self.l = 0
        self.r = self.n-1
        self.root = self._make_tree(nums, self.l, self.r)

    def _make_tree(self, nums, l, r):
        if l == r:
            return Node(nums[l])
        
        node = Node()
        mid = (l+r) // 2
        node.left = self._make_tree(nums, l, mid)
        node.right = self._make_tree(nums, mid+1, r)
        node.val = node.left.val + node.right.val
        return node
    
    def update(self, index, val):

        def update_helper(node, l, r):
            if l == r:
                node.val = val
                return
            
            mid = (l+r) // 2
            if index <= mid:
                update_helper(node.left, l, mid)
            else:
                update_helper(node.right, mid+1, r)
            
            node.val = node.left.val + node.right.val
        
        update_helper(self.root, self.l, self.r)

    def sum_range(self, start, stop):
        
        def sum_range_helper(node, l, r, i, j):
            if l == i and r == j:
                return node.val

            mid = (l+r) // 2
            if j <= mid:
                return sum_range_helper(node.left, l, mid, i, j)
            elif i >= mid+1:
                return sum_range_helper(node.right, mid+1, r, i, j)

            left_sum = sum_range_helper(node.left, l, mid, i, mid)
            right_sum = sum_range_helper(node.right, mid+1, r, mid+1, j)
            
            return left_sum + right_sum
        
        return sum_range_helper(self.root, self.l, self.r, start, stop)

class NumArray:

    def __init__(self, nums: List[int]):
        self.segment_tree = SegmentTree(nums)

    def update(self, index: int, val: int) -> None:
        self.segment_tree.update(index, val)
        
    def sumRange(self, left: int, right: int) -> int:
        return self.segment_tree.sum_range(left, right)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)


class Node:
    def __init__(self, val=None, left=None, right=None, start=None, stop=None):
        self.val = val
        self.left = left
        self.right = right
        self.start = start
        self.stop = stop

class SegmentTree:
    def __init__(self, nums):
        self.root = self._make_tree(nums, 0, len(nums)-1)

    def _make_tree(self, nums, l, r):
        if l == r:
            return Node(val=nums[l], start=l, stop=r)
        
        node = Node(start=l, stop=r)
        mid = (l+r) // 2
        node.left = self._make_tree(nums, l, mid)
        node.right = self._make_tree(nums, mid+1, r)
        node.val = node.left.val + node.right.val
        return node
    
    def update(self, index, val):

        def update_helper(node):
            if node.start == node.stop:
                node.val = val
                return
            
            mid = (node.start + node.stop) // 2
            if index <= mid:
                update_helper(node.left)
            else:
                update_helper(node.right)
            
            node.val = node.left.val + node.right.val
        
        update_helper(self.root)

    def sum_range(self, start, stop):
        
        def sum_range_helper(node, i, j):
            if node.start == i and node.stop == j:
                return node.val

            mid = (node.start + node.stop) // 2
            if j <= mid:
                return sum_range_helper(node.left, i, j)
            elif i >= mid+1:
                return sum_range_helper(node.right, i, j)

            left_sum = sum_range_helper(node.left, i, mid)
            right_sum = sum_range_helper(node.right, mid+1, j)
            
            return left_sum + right_sum
        
        return sum_range_helper(self.root, start, stop)

class NumArray:

    def __init__(self, nums: List[int]):
        self.segment_tree = SegmentTree(nums)

    def update(self, index: int, val: int) -> None:
        self.segment_tree.update(index, val)
        
    def sumRange(self, left: int, right: int) -> int:
        return self.segment_tree.sum_range(left, right)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)

class Node:
    def __init__(self, val=None, left=None, right=None, start=None, stop=None):
        self.val = val
        self.left = left
        self.right = right
        self.start = start
        self.stop = stop

class SegmentTree:
    def __init__(self, nums):
        self.nums = nums
        self.root = self._make_tree(nums, 0, len(nums)-1)

    def _make_tree(self, nums, l, r):
        if l == r:
            return Node(val=nums[l], start=l, stop=r)
        
        node = Node(start=l, stop=r)
        mid = (l+r) // 2
        node.left = self._make_tree(nums, l, mid)
        node.right = self._make_tree(nums, mid+1, r)
        node.val = node.left.val + node.right.val
        return node
    
    def update(self, index, val):
        diff = self.nums[index] - val
        self.nums[index] = val

        def update_helper(node):
            if not node or index > node.stop or index < node.start:
                return
            if node.start <= index <= node.stop:
                node.val -= diff

            update_helper(node.left)
            update_helper(node.right)
        
        update_helper(self.root)

    def sum_range(self, start, stop):
        
        def sum_range_helper(node):
            if not node or start > node.stop or stop < node.start:
                return 0
            if node.start >= start and node.stop <= stop:
                return node.val

            left_sum = sum_range_helper(node.left)
            right_sum = sum_range_helper(node.right)
            
            return left_sum + right_sum
        
        return sum_range_helper(self.root)

class NumArray:

    def __init__(self, nums: List[int]):
        self.segment_tree = SegmentTree(nums)

    def update(self, index: int, val: int) -> None:
        self.segment_tree.update(index, val)
        
    def sumRange(self, left: int, right: int) -> int:
        return self.segment_tree.sum_range(left, right)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)


from itertools import accumulate
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.n = len(nums)
        self.bit = [0] * (self.n+1) # bit is binary index tree
        self._build_bit()
    
    def _build_bit(self):
        for i in range(1, self.n+1):
            self.bit[i] += self.nums[i-1]
            next = i + (i & -i) # i + right_most_set_bit
            if next <= self.n:
                self.bit[next] += self.bit[i]


    def update(self, index: int, val: int) -> None:
        diff = val - self.nums[index]
        self.nums[index] = val
        index += 1 # bit index starts from 1
        while index <= self.n:
            self.bit[index] += diff
            index += index & -index # next

        
    def sumRange(self, left: int, right: int) -> int:
        
        def prefix_sum(index):
            total = 0
            while index > 0:
                total += self.bit[index]
                index -= index & -index # parent
            return total
        
        return prefix_sum(right + 1) - prefix_sum(left)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)


# learnings from below links:
# https://www.youtube.com/watch?v=CWDQJGaN1gY
# https://www.geeksforgeeks.org/fenwick-tree-for-competitive-programming/
# https://www.geeksforgeeks.org/binary-indexed-tree-or-fenwick-tree-2/
# https://www.geeksforgeeks.org/twos-complement/
# https://leetcode.com/problems/range-sum-query-mutable/solutions/1406686/c-java-python-3-solutions-sqrt-decomposition-binary-indexed-tree-segment-tree

