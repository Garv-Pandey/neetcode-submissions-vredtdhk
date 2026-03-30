# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        result = ""

        def dfs(node):
            nonlocal result
            if not node:
                result += "N,"
                return

            result += f"{node.val},"

            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return result
        
    # Decodes your encoded data to tree.
    
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None

        data_arr = data.split(",")[:-1]

        self.index = 0

        def dfs():

            if data_arr[self.index] == "N":
                self.index+=1
                return None
            
            node = TreeNode(int(data_arr[self.index]))
            self.index+=1
            node.left = dfs()
            node.right = dfs()

            return node

        return dfs() 