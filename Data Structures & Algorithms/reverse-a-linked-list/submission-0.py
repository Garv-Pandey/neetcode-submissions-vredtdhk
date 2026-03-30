# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr_point = head
        prev_point = None

        while curr_point != None:
            next_node = curr_point.next
            curr_point.next = prev_point

            prev_point = curr_point
            curr_point = next_node

        return prev_point