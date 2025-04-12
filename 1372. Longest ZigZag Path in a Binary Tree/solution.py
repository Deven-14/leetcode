# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        zig_zag = 0

        def helper(root):
            nonlocal zig_zag
            if not root:
                return (-1, -1)
            
            (ll, lr) = helper(root.left)

            (rl, rr) = helper(root.right)

            zig_zag = max(zig_zag, ll, (1 + lr), (1 + rl), rr)

            return (1 + lr), (1 + rl)
        
        helper(root)
        return zig_zag


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:

        def helper(root):
            if not root:
                return 0, (-1, -1)
            
            l_zig_zag, (ll, lr) = helper(root.left)

            r_zig_zag, (rl, rr) = helper(root.right)

            zig_zag = max(l_zig_zag, r_zig_zag, ll, (1 + lr), (1 + rl), rr)

            return zig_zag, ((1 + lr), (1 + rl))
        
        zig_zag, _ = helper(root)
        return zig_zag



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        
        def helper(root, left, right):
            if not root:
                return max(left, right)
            
            l_zig_zag = helper(root.left, -1, left + 1)

            r_zig_zag = helper(root.right, right + 1, -1)

            return max(l_zig_zag, r_zig_zag)
        
        return helper(root, -1, -1)



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.zig_zag = 0

        def helper(root):
            if not root:
                return (-1, -1)
            
            (_, lr) = helper(root.left)

            (rl, _) = helper(root.right)

            self.zig_zag = max(self.zig_zag, (1 + lr), (1 + rl))

            return (1 + lr), (1 + rl)
        
        helper(root)
        return self.zig_zag



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        zig_zag = 0

        def helper(root):
            nonlocal zig_zag
            if not root:
                return (-1, -1)
            
            _, lr = helper(root.left)

            rl, _ = helper(root.right)

            zig_zag = max(zig_zag, 1 + lr, 1 + rl)

            return 1 + lr, 1 + rl
        
        helper(root)
        return zig_zag


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        stack = [(root, 0, 0)]
        zig_zag = 0

        while stack:
            node, zig, zag = stack.pop()

            zig_zag = max(zig_zag, zig, zag)

            if node.left:
                stack.append((node.left, zag + 1, 0))
            
            if node.right:
                stack.append((node.right, 0, zig + 1))
        
        return zig_zag


