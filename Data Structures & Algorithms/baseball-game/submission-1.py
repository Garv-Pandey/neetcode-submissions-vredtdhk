class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for p in operations:
            if p == '+':
                stack.append(stack[-1]+stack[-2])

            elif p=='C':
                stack.pop()

            elif p == 'D':
                stack.append(stack[-1]*2)

            else: 
                stack.append(int(p))

        return sum(stack)