# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        def dfs(root):
            if not root:
                return {"with_root":0, "without_root":0}
            lst = dfs(root.left)
            rst = dfs(root.right)

            curr_node = {}
            curr_node["with_root"]= root.val + lst["without_root"] + rst["without_root"]
            curr_node["without_root"]= max(lst["with_root"], lst["without_root"]) + max(rst["with_root"], rst["without_root"])

            return curr_node
        
        print(dfs(root))
        return max(dfs(root).values())
