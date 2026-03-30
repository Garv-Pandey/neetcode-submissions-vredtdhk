# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_node = ListNode()
        curr_node = dummy_node
        num1 = l1
        num2 = l2
        remainder = 0

        while num1 or num2 or remainder:
            val1 = num1.val if num1 else 0
            val2 = num2.val if num2 else 0
            total = val1 + val2 + remainder

            num = total%10
            remainder = total//10
            
            curr_node.next = ListNode(num, None)
            curr_node = curr_node.next

            num1 = num1.next if num1 else num1
            num2 = num2.next if num2 else num2

        return dummy_node.next