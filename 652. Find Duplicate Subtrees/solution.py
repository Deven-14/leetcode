# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        subtrees = set()
        duplicate_roots = {}

        def preorder(node):
            if not node:
                return "$#"
            
            if not node.left and not node.right:
                return f"${node.val}"
            
            l = preorder(node.left)
            if l in subtrees:
                duplicate_roots[l] = node.left
            else:
                subtrees.add(l)
            
            r = preorder(node.right)
            if r in subtrees:
                duplicate_roots[r] = node.right
            else:
                subtrees.add(r)
            
            return f"${node.val}{l}{r}"
        
        preorder(root)
        return [node for node in duplicate_roots.values() if node != None]


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        subtrees = Counter()
        duplicate_roots = []

        def postorder(node):
            if not node:
                return "$#"
            
            l = postorder(node.left)
            r = postorder(node.right)
            t = f"${node.val}{l}{r}"

            subtrees[t] += 1
            if subtrees[t] == 2:
                duplicate_roots.append(node)
            
            return t
        
        postorder(root)
        return duplicate_roots



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        subtrees = Counter()
        duplicate_roots = []

        def postorder(node):
            if not node:
                return ()
            
            l = postorder(node.left)
            r = postorder(node.right)
            t = (node.val, l, r)

            subtrees[t] += 1
            if subtrees[t] == 2:
                duplicate_roots.append(node)
            
            return t
        
        postorder(root)
        return duplicate_roots


