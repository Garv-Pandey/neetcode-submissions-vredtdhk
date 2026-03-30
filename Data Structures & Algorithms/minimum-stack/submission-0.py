class MinStack:

    def __init__(self):
        self.value_stack = list()  # keeps track of values being added
        self.min_stack = (
            list()
        )  # keeps track of min value available in stack up until each node

    def push(self, val: int) -> None:
        self.value_stack.append(val)

        if (
            len(self.min_stack) == 0
        ):  # if min_stack is empty i.e., this is the first element being added to MinStack object
            self.min_stack.append(val)
            return

        # if min_stack is not empty, comparing the current value being added and the top value in min_stack of the object
        min_val = min(self.min_stack[-1], val)
        self.min_stack.append(min_val)

        return

    def pop(self) -> None:
        self.value_stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.value_stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
