class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dic = Counter(magazine)
        for c in ransomNote:
            if c not in magazine or dic[c] == 0:
                return False
            dic[c] -= 1
        return True