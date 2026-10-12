class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        if len(pattern) != len(words):
            return False
        charToWords, wordsToChars = {}, {}
        for c, w in zip(pattern, words):
            if c in charToWords and charToWords[c] != w:
                return False
            if w in wordsToChars and wordsToChars[w] != c:
                return False
            charToWords[c] = w
            wordsToChars[w] = c
        return True