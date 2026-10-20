class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        cnt = len(words)
        allowed = set(allowed)
        for w in words:
            for c in w:
                if c not in allowed:
                    cnt -= 1
                    break
        return cnt