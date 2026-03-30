# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        result = root.val

        def dfs(node):
            if not node:
                return 0

            no_split_left_sum = dfs(node.left)
            no_split_right_sum = dfs(node.right)

            split_sum = no_split_left_sum + node.val + no_split_right_sum
            nonlocal result
            result = max(result, split_sum)

            return max(node.val + no_split_left_sum, 
                        node.val + no_split_right_sum,
                        0)
        
        dfs(root)
        return result