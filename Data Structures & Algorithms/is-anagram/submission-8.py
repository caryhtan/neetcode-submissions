class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dic = {}
        for char in s:
            dic[char] = dic.get(char, 0) + 1
        for char in t:
            if char not in dic or dic.get(char) == 0:
                return False
            dic[char] -= 1
        return True