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
        if not head:
            return head
            
        old_new = dict()

        curr_node = head
        while curr_node:
            old_new[curr_node] = Node(curr_node.val)
            curr_node = curr_node.next

        curr_node = head
        while curr_node:
            old_new[curr_node].next = old_new.get(curr_node.next, None)
            old_new[curr_node].random = old_new.get(curr_node.random, None)
            curr_node = curr_node.next

        return old_new[head]