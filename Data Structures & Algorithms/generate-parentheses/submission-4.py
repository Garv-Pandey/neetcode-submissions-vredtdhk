class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        answer = []
        
        stack = []

        def paran(open_count, close_count):
            if open_count == close_count==n:
                answer.append(''.join(stack))

            if open_count<n:
                stack.append('(')
                paran(open_count+1, close_count)
                stack.pop()

            if close_count<open_count:
                stack.append(')')
                paran(open_count, close_count+1)
                stack.pop()

        paran(0,0)

        return answer