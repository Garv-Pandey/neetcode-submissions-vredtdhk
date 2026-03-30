# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy_node = ListNode(0, head)
        prev = dummy_node
        curr = head
        for _ in range(left-1):
            prev = prev.next
            curr = curr.next

        start = curr
        start_prev = prev

        curr = curr.next
        prev = prev.next

        for _ in range(right - left ):
            temp = curr.next
            
            curr.next = prev
            
            prev = curr
            curr = temp

        end = prev
        end_next = curr

        start_prev.next = end
        start.next = end_next

        return dummy_node.next 