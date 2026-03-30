class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        answer = []
        def parenBuilder(open_count, close_count):
            if open_count == close_count == n:
                answer.append(''.join(stack))
                return

            if open_count < n:
                stack.append('(')
                parenBuilder(open_count + 1, close_count)
                stack.pop()

            if close_count < open_count:
                stack.append(')')
                parenBuilder(open_count, close_count+1)
                stack.pop()

        parenBuilder(0,0)
        return answer