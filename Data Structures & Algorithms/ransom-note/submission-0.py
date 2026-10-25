class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dic = Counter(magazine)
        for i, c in enumerate(ransomNote):
            if dic[c] == 0:
                return False
            dic[c] -= 1
        return True