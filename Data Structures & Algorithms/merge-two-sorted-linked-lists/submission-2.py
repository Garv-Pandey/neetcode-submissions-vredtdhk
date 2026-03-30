# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        point_1 = list1
        point_2 = list2

        dummy_node = ListNode()
        curr = dummy_node

        while point_1 and point_2:
            if point_1.val <= point_2.val:
                curr.next = point_1

                curr = point_1
                point_1 = point_1.next

            else:
                curr.next = point_2

                curr = point_2
                point_2 = point_2.next

        curr.next = point_1 or point_2

        return dummy_node.next