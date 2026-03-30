# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return [] 

        result = list()
        order = collections.deque([root])

        while order:
            curr_level_ele_no = len(order)
            curr_level_ele = list()
            for i in range(curr_level_ele_no):
                curr_ele = order.popleft()

                if curr_ele is None:
                    continue

                order.append(curr_ele.left)
                order.append(curr_ele.right)
                curr_level_ele.append(curr_ele.val)

            if curr_level_ele :
                result.append(curr_level_ele)
        
        return result

        