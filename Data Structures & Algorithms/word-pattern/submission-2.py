class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        if len(pattern) != len(words):
            return False
        dic1, dic2 = {}, {}
        for c, w in zip(pattern, words):
            if c in dic1 and dic1[c] != w:
                return False
            if w in dic2 and dic2[w] != c:
                return False
            dic1[c] = w
            dic2[w] = c
        return True