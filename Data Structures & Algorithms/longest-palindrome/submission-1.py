class Solution:
    def longestPalindrome(self, s: str) -> int:
        seen = set()
        cnt = 0
        for c in s:
            if c not in seen:
                seen.add(c)
            else:
                seen.remove(c)
                cnt += 2
        if len(seen) > 0:
            return cnt + 1
        else:
            return cnt