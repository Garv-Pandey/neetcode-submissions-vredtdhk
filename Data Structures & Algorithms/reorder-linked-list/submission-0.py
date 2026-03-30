# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # finding first node to start reversing from (middle or first middle)
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev_node = None
        curr_node = slow.next
        slow.next = None
        while curr_node:
            temp = curr_node.next
            
            curr_node.next = prev_node

            prev_node = curr_node
            curr_node = temp

        l_node= head
        r_node = prev_node
        while l_node and r_node:
            l_temp = l_node.next
            r_temp = r_node.next

            l_node.next = r_node
            r_node.next = l_temp

            l_node = l_temp
            r_node = r_temp