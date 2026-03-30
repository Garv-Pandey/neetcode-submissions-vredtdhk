class NodeList:
    def __init__(self, val=0, next=None, prev = None):
        self.value = val
        self.next = next
        self.prev = prev

class MyCircularQueue:

    def __init__(self, k: int):
        self.capacity = k
        self.count = 0
        self.front = NodeList()
        self.back = NodeList()

        self.front.next = self.back
        self.back.prev = self.front

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False

        new_node = NodeList(value, self.back, self.back.prev)
        self.back.prev.next = new_node
        self.back.prev = new_node

        self.count += 1

        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        
        remove_node = self.front.next

        self.front.next = remove_node.next
        remove_node.next.prev = self.front

        remove_node.next = remove_node.prev = None
        del remove_node

        self.count -= 1

        return True
        
    def Front(self) -> int:
        if self.isEmpty():
            return -1

        return self.front.next.value

    def Rear(self) -> int:
        if self.isEmpty():
            return -1

        return self.back.prev.value

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.capacity


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()