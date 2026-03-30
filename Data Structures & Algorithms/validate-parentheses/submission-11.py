class Solution:
    def isValid(self, s: str) -> bool:
        closeOpen_match = {')':'(', ']':'[','}':'{'}
        stack = []

        for brack in s:
            if brack not in closeOpen_match:
                stack.append(brack)
                continue

            if not stack or stack[-1] != closeOpen_match[brack]:
                return False

            stack.pop()
            
        return len(stack) == 0