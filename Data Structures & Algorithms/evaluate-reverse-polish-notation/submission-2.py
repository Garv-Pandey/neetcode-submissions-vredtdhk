class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = list()
        
        for token in tokens: 
            if token not in ['+','-','*','/']:
                stack.append(token)
                continue

            b = stack.pop()
            a = stack.pop()
            expression = a + token + b
            new_token = str(int(eval(expression))) # using int() to round the result towards 0
            stack.append(new_token)
            
        return int(stack[0])