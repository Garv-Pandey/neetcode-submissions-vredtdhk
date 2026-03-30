class MinStack:

    def __init__(self):
        self.stack = []
        self.min_value_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if len(self.min_value_stack) == 0:
            self.min_value_stack.append(val)
            return
        
        if val <= self.min_value_stack[-1]:
            self.min_value_stack.append(val)

    def pop(self) -> None:
        a = self.stack.pop()
        if self.min_value_stack[-1] == a:
            self.min_value_stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_value_stack[-1]
        
