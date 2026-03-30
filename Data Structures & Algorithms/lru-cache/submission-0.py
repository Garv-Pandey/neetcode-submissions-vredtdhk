class Node:
    def __init__(self, key, value, next = None, prev = None) -> None:
        self.key = key
        self.value = value
        self.next = next
        self.prev = prev


class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        # building dictionary
        self.key_node = dict()

        # building linked list
        self.low = Node(0,0)
        self.high = Node(0,0)

        self.low.next = self.high
        self.high.prev = self.low
        

    def remove (self, node_address):
        prev = node_address.prev
        next = node_address.next

        prev.next = next
        next.prev = prev

        node_address.next, node_address.prev = None, None

    # insert the node before high
    def insert (self, node_address, high_address):
        node_address.next = high_address
        node_address.prev = high_address.prev
        high_address.prev.next = node_address
        high_address.prev = node_address
    
    
    def get(self, key: int) -> int:
        if key not in self.key_node:
            return -1

        # removing the node from whereever it is and putting it before high
        node_address = self.key_node[key]

        self.remove(node_address)
        self.insert( node_address, self.high)
        return node_address.value

    def put(self, key: int, value: int) -> None:

        if key in self.key_node: 
            node_address = self.key_node[key]

            node_address.value = value
            self.remove(node_address)
            self.insert(node_address, self.high)
            return 
        
        if len(self.key_node) == self.cap:
            to_remove_key = self.low.next.key
            del self.key_node[to_remove_key]
            self.remove(self.low.next)
        
        new = Node(key, value)

        self.key_node[key] = new

        self.insert(new, self.high)
        return