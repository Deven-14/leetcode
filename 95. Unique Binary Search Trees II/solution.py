from itertools import permutations
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        all_permutations = permutations(range(1, n+1))
        trees = []

        def add_node(root, value):
            if root == None:
                return TreeNode(value)
            elif value > root.val:
                root.right = add_node(root.right, value)
            elif value < root.val:
                root.left = add_node(root.left, value)
            return root

        def generateTree(permutation):
            root = TreeNode(permutation[0])
            for num in permutation[1:]:
                root = add_node(root, num)
            return root
        
        def inorder(root, inorder_tree):
            if not root:
                inorder_tree.append(None)
                return 
            inorder_tree.append(root.val)
            inorder(root.left, inorder_tree)
            inorder(root.right, inorder_tree)
        
        inorder_trees = set()
        for permutation in all_permutations:
            tree = generateTree(permutation)
            inorder_tree = []
            inorder(tree, inorder_tree)
            inorder_tree = tuple(inorder_tree)
            if inorder_tree not in inorder_trees:
                trees.append(tree)
                inorder_trees.add(inorder_tree)
        
        return trees


from functools import cache
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        
        @cache
        def generateTreesHelper(start, end):
            trees = []
            for root_val in range(start, end):
                for left_tree in generateTreesHelper(start, root_val):
                    for right_tree in generateTreesHelper(root_val+1, end):
                        root = TreeNode(root_val)
                        root.left = left_tree
                        root.right = right_tree
                        trees.append(root)
            
            return trees or [None]
        
        return generateTreesHelper(1, n+1)