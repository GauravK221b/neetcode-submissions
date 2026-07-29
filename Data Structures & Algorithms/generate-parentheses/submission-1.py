class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def backtrac(openN, closeN):
            if openN == closeN == n:
                res.append("".join(stack))
                return
            
            if openN < n:
                stack.append("(")
                backtrac(openN+1, closeN)
                stack.pop()
            
            if closeN < openN:
                stack.append(")")
                backtrac(openN, closeN+1)
                stack.pop()

        backtrac(0,0)
        return res