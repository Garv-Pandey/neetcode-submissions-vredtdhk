# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def traverse(root, current_depth):
            if not root:
                return current_depth
            
            left = traverse(root.left, current_depth+1)
            right = traverse(root.right, current_depth+1)

            return max(left, right)
            
            
        left = traverse(root.left, 1)
        right = traverse(root.right, 1)

        return max(left, right)

