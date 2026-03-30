class Solution:
    def isValid(self, s: str) -> bool:
        stack= []
        closeOpen_pair = {')':'(', '}':'{', ']':'['}

        for brack in s:
            if brack not in closeOpen_pair:
                stack.append(brack)
                continue

            if not stack or stack[-1] != closeOpen_pair[brack]:
                return False

            stack.pop()

        return len(stack)==0




