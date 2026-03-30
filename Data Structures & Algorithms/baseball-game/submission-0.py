class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score_stack = []

        for op in operations:
            if op == '+':
                a = score_stack.pop()
                b = score_stack.pop()

                score_stack.append(b)
                score_stack.append(a)
                score_stack.append(a+b)

            elif op == 'C':
                score_stack.pop()

            elif op == 'D':
                a = score_stack.pop()
                score_stack.append(a)
                score_stack.append(a*2)

            else: 
                score_stack.append(int(op))

            print(score_stack)

        return(sum(score_stack))