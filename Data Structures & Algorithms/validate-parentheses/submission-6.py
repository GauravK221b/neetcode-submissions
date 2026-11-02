class Solution:
    def isValid(self, s: str) -> bool:
        res = []
        hashSet = {")" : "(",
                    "}" : "{",
                    "]" : "["}
        
        for c in s:
            if c in ['{', '(', '[']:
                res.append(c)
            else:
                if not res or res[-1] != hashSet[c]:
                    return False
                else:
                    res.pop()
        return len(res) == 0