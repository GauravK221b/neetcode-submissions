class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        freq_s1 = {}
        freq_s2 = {}
        for r in range(len(s1)):
            freq_s1[s1[r]] = 1 + freq_s1.get(s1[r],0)
        for r in range(len(s2)):
            freq_s2[s2[r]] = 1 + freq_s2.get(s2[r], 0)
            if r - l + 1 > len(s1):
                freq_s2[s2[l]] -= 1
                if freq_s2[s2[l]] == 0:
                    del freq_s2[s2[l]]
                l += 1
            if r - l + 1 == len(s1):
                if freq_s1 == freq_s2:
                    return True
            

        return False
