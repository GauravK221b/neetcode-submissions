class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operator = ['+', '-', '*', '/']
        stack = []

        for char in tokens:
            if char in operator:
                op2 = stack.pop()
                op1 = stack.pop()
                if char == '+':
                    
                    stack.append(op1 + op2)
                elif char == '-':
                   
                    stack.append(op1 - op2)
                elif char == '*':
                    
                    stack.append(op1 * op2)
                else:
                    
                    stack.append(int(op1 / op2))
            else:
                stack.append(int(char))
        
        return stack[-1]