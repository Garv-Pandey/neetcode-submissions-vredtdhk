class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = list()
        results = list()
        
        open_bracks = 0
        close_bracks = 0
        def pattern_former(open_bracks, close_bracks):
            if open_bracks == close_bracks == n:
                result = "".join(stack)
                results.append(result)
                return

            if open_bracks < n:
                stack.append("(")
                pattern_former(open_bracks + 1, close_bracks)
                stack.pop()

            if close_bracks < open_bracks:
                stack.append(")")
                pattern_former(open_bracks, close_bracks + 1)
                stack.pop()

        pattern_former(0,0)
        return results