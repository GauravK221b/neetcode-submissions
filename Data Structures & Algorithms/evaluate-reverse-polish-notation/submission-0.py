class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []

        operators = {'+', '-', '*', '/'}

        for c in tokens:

            if c in operators:

                op2 = stack.pop()
                op1 = stack.pop()

                if c == '+':
                    res = op1 + op2

                elif c == '-':
                    res = op1 - op2

                elif c == '*':
                    res = op1 * op2

                else:
                    res = int(op1 / op2)

                stack.append(res)

            else:
                stack.append(int(c))

        return stack[-1]
        