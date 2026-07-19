class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dic = {}
        for c in s:
            dic[c] = dic.get(c, 0) + 1
        for c in t:
            # A key can still exist in dic even when its value is 0.
            if c not in dic or dic[c] == 0:
                return False
            else:
                dic[c] -= 1
        return True