class ListNode:
    def __init__(self, key = None, value = 0, next = None, prev = None) -> None:
        self.key = key
        self.value = value
        self.next = next
        self.prev = prev


class LRUCache:

    def __init__(self, capacity: int):
        self.count = 0
        self.capacity = capacity

        self.key_value = dict()
        self.key_address = dict()

        self.least_node = ListNode()
        self.most_node = ListNode()

        self.least_node.next = self.most_node
        self.most_node.prev = self.least_node

    def get(self, key: int) -> int:
        if key not in self.key_value:
            return -1

        key_node = self.key_address[key]
        key_node.prev.next = key_node.next 
        key_node.next.prev = key_node.prev

        key_node.next = self.most_node
        key_node.prev = self.most_node.prev

        self.most_node.prev.next = key_node
        self.most_node.prev = key_node

        return self.key_value[key] 

    def put(self, key: int, value: int) -> None:
        if key in self.key_value:
            self.key_value[key] = value

            key_node = self.key_address[key]
            key_node.value = value

            key_node.prev.next = key_node.next 
            key_node.next.prev = key_node.prev

            key_node.next = self.most_node
            key_node.prev = self.most_node.prev

            self.most_node.prev.next = key_node
            self.most_node.prev = key_node

            return

        # if key is not present and the cache is full, removing the least frequent node to make space
        if self.count == self.capacity:
            remove_key = self.least_node.next.key
            remove_node = self.least_node.next

            # removing the node
            self.least_node.next = remove_node.next
            remove_node.next.prev = self.least_node

            del remove_node

            # removing entries from key_value and key_address dicts
            del self.key_value[remove_key]
            del self.key_address[remove_key]

            # setting counters
            self.count -= 1


        # inserting the new key-value pair in cache
        # inserting the node
        new_node = ListNode(key, value, self.most_node, self.most_node.prev)
        self.most_node.prev.next = new_node
        self.most_node.prev = new_node

        # inserting key-value pair in dicts
        self.key_value[key] = value
        self.key_address[key] = new_node

        # incrementing counter
        self.count += 1

        return