class Solution:
    def isValid(self, s: str) -> bool:
        close_open ={
            ')' : '(',
            '}' : '{',
            ']' : '['
        }

        stack = []

        for br  in s:
            if br in close_open:
                if not stack:
                    return False
                top = stack.pop()
                if top != close_open[br]:
                    return False
            else:
                stack.append(br)
        
        if stack:
            return False
        return True
