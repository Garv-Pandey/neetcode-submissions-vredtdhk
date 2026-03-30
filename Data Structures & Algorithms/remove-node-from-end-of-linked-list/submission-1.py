# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy_node = ListNode(0, head)
        forw_node = dummy_node
        back_node = dummy_node

        for i in range(n+1):
            forw_node = forw_node.next

        while forw_node:
            forw_node = forw_node.next
            back_node = back_node.next

        back_node.next = back_node.next.next

        return dummy_node.next