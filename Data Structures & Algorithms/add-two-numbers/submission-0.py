# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_node = ListNode()
        curr_node = dummy_node
        carry = 0
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            total = val1+val2+carry

            carry = total//10
            node_val = total%10
            curr_node.next = ListNode(node_val)

            curr_node = curr_node.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy_node.next