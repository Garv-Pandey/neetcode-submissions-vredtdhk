"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        address_map = dict() #old_address: new_address
        address_map[None] = None #to handle edge case when random points to none
        old_curr = head
        while old_curr:
            new_curr = Node(old_curr.val, None, None)
            address_map[old_curr] = new_curr
            old_curr = old_curr.next

        old_curr = head
        new_curr = address_map[old_curr]
        while old_curr:
            new_curr.next = address_map[old_curr.next]
            new_curr.random = address_map[old_curr.random]
            old_curr = old_curr.next
            new_curr = new_curr.next

        return address_map[head]