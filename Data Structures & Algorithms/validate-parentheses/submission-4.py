class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()
        bracket_map = {')':'(', ']':'[', '}':'{'}

        for char in s: # string only contains open and close brackets
            if char not in bracket_map: # when we encounter open bracket
                stack.append(char)
                continue

            if len(stack) == 0 or stack[-1] != bracket_map.get(char): # when we encounter close bracket. Here we need to find the open bracket based on type of close bracket. thats why the keys of dictionary are closed brackets 
                return False

            # if stack is not empty and the current char properly closes the top element of stack
            stack.pop()

        if len(stack) != 0:
            return False
        
        return True 