# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_node = ListNode()
        curr_node = dummy_node

        while list1 != None and list2 != None:
            if list1.val <= list2.val:
                curr_node.next = list1
                list1 = list1.next

            else:
                curr_node.next = list2
                list2 = list2.next

            curr_node = curr_node.next

        curr_node.next = list1 or list2

        return dummy_node.next