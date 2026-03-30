class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        answer = []
        def paranGene (open_count, close_count):
            if open_count == close_count == n :
                answer.append(''.join(stack))
                return

            if open_count < n:
                stack.append("(")
                paranGene(open_count + 1, close_count)
                stack.pop()

            if close_count < open_count:
                stack.append(")")
                paranGene(open_count, close_count + 1)
                stack.pop()

        paranGene(0, 0)
        return answer