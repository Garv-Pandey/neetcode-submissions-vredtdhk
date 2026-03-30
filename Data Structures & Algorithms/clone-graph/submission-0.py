"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return 
        
        node_map = {}

        def clone(node):
            if node in node_map:
                return node_map[node]
            
            clone_node = Node(node.val)

            node_map[node] = clone_node
            for neighbor in node.neighbors:
                clone_node.neighbors.append(clone(neighbor))
            
            return clone_node
        
        return clone(node)