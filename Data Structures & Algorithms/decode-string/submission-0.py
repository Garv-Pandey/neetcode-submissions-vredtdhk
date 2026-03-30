class Solution:
    def decodeString(self, s: str) -> str:
        string_stack = []

        for char in s:
            if char != ']':
                string_stack.append(char)

            else:
                substring = ""
                while string_stack[-1] != '[':
                    substring = string_stack.pop() + substring

                string_stack.pop()

                multiplier = ""
                while string_stack and string_stack[-1].isdigit():
                    multiplier = string_stack.pop() + multiplier

                string_stack.append(int(multiplier) * substring)

        return "".join(string_stack)