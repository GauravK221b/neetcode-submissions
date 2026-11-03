class Solution:
    def isValid(self, s: str) -> bool:
        hashMap = {')' : '(',
                    '}' : '{',
                    ']' : '['}
        stack = []
        for c in s:
            if c in ['(', '{', '[']:
                stack.append(c)
            else:
                if not stack or stack[-1] != hashMap[c]:
                    return False
                else:
                    stack.pop()
        
        return (len(stack) == 0)
            
