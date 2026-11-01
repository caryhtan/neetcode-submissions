class Solution:
    def longestPalindrome(self, s: str) -> int:
        seen = set()
        res = 0
        for c in s:
            if c not in seen:
                seen.add(c)
                continue
            seen.remove(c)
            res += 2
        return res + 1 if seen else res