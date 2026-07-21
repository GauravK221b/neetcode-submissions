class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        store1 = [s[0]]
        store2 = [t[0]]
        for i in range(1, len(s)):
            store1.append(s[i])
            store2.append(t[i])
        store1.sort()
        store2.sort()
        if store1 == store2:
            return True
        return False