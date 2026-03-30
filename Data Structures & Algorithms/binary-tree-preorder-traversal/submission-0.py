# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        order = []

        def traversal(root):

            if not root:
                return 

            order.append(root.val)

            if root.left:
                traversal(root.left)
            
            if root.right:
                traversal(root.right)

        traversal(root)
        return order
