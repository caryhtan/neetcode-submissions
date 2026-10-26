class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dic = Counter(s)
        for c in t:
            if c not in dic or dic.get(c) == 0:
                return False
            dic[c] -= 1
        return True