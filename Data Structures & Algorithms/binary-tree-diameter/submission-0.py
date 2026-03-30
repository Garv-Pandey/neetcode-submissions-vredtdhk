# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0


        result = 0
        def depth(root, current_level):
            if not root:
                return 0

            left = depth(root.left, current_level+1)
            right = depth(root.right, current_level+1)

            nonlocal result
            result = max(result, left+right)
            return 1+ max(left, right)

        depth(root, 0)

        return result