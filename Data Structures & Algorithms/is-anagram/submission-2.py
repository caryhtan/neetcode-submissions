class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dic = {}
        for c in s:
            dic[c] = dic.get(c, 0) + 1
        for c in t:
            if c not in dic or dic[c] == 0:
                return False
            dic[c] -= 1
        return True