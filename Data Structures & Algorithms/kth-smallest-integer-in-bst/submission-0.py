# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        sorted_arr = []

        def dfs_inorder(root):
            if not root:
                return None
            
            dfs_inorder(root.left)
            sorted_arr.append(root.val)
            dfs_inorder(root.right)
        
        dfs_inorder(root)
        return sorted_arr[k-1]