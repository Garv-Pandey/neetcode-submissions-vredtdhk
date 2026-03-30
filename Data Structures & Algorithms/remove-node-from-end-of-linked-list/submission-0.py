# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy_node = ListNode(0,head)
        prev_node = dummy_node
        curr_node = head

        leading_node = head
        for i in range(n):
            leading_node=leading_node.next

        while leading_node:
            prev_node = prev_node.next
            curr_node = curr_node.next
            leading_node = leading_node.next

        prev_node.next = curr_node.next
        curr_node.next = None

        return dummy_node.next