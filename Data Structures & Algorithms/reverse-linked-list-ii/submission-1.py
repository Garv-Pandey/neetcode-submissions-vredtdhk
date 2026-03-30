# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy_node = ListNode(0, head)
        start = dummy_node
        curr = head

        count1 = 1
        while count1<left:
            start= start.next
            curr = curr.next
            count1 += 1

        prev = curr
        curr = curr.next
        count1 += 1
        while count1 <= right:
            temp = curr.next

            curr.next = prev

            prev = curr
            curr = temp 
            count1 +=1

        start.next.next = curr
        start.next = prev

        return dummy_node.next