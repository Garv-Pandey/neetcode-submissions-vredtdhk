class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()

        for char in s:
            if char in ["(", "{", "["]:
                stack.append(char)

            match char:
                case ")":
                    if len(stack) == 0 or stack.pop() != "(":
                        return False

                case "]":
                    if len(stack) == 0 or stack.pop() != "[":
                        return False

                case "}":
                    if len(stack) == 0 or stack.pop() != "{":
                        return False

        if len(stack) != 0:
            return False
            
        return True