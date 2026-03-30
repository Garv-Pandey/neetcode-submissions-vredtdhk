# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self) -> None:
        self.order = []

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
            
        if root.left:
            self.inorderTraversal(root.left)
        
        self.order.append(root.val)

        if root.right:
            self.inorderTraversal(root.right)
        
        return self.order
