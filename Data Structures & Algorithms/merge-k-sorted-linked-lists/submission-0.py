# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None
        
        merged_lists = lists

        while len(merged_lists) > 1:
            temp = []

            for i in range(0, len(merged_lists), 2):
                list1 = merged_lists[i]
                list2 = merged_lists[i+1] if i+1 < len(merged_lists) else None

                temp.append(self.merge(list1, list2))

            merged_lists = temp

        return merged_lists[0]

        
    def merge(self, list1, list2):
        dummy_node = ListNode()
        curr_node = dummy_node
        while list1 and list2:
            if list1.val <= list2.val:
                curr_node.next = list1
                list1 = list1.next

            else:
                curr_node.next = list2
                list2 = list2.next

            curr_node = curr_node.next

        curr_node.next = list1 or list2

        return dummy_node.next