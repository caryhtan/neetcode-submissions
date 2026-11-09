class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sCnt = Counter(s)
        for c in t:
            if c not in sCnt or sCnt[c] == 0:
                return False
            sCnt[c] -= 1
        return True