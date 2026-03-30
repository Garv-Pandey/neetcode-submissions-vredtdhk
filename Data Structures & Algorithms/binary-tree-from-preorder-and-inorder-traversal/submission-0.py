# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        root_val = preorder[0]

        inorder_lst = inorder[ : inorder.index(root_val)]
        inorder_rst = inorder[inorder.index(root_val)+1 : ]
        preorder_lst = preorder[1 : 1 + len(inorder_lst)]
        preorder_rst = preorder[1 + len(inorder_lst) : ]

        print(root_val, preorder_lst, preorder_rst)
        print(root_val, inorder_lst, inorder_rst)


        root_node = TreeNode(root_val, None, None)
        root_node.left = self.buildTree(preorder_lst, inorder_lst)
        root_node.right = self.buildTree(preorder_rst, inorder_rst)

        return root_node