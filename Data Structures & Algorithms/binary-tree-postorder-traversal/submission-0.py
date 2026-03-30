# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        order = []

        def travers(root):
            if not root:
                return
            
            if root.left:
                travers(root.left)
            
            if root.right:
                travers(root.right)
            
            order.append(root.val)
        
        travers(root)
        return order