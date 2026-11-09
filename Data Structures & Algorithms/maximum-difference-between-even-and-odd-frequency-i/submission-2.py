class Solution:
    def maxDifference(self, s: str) -> int:
        cnt = Counter(s)
        minEven, maxOdd = float('inf'), 0
        for v in cnt.values():
            if v % 2 == 0:
                minEven = min(v, minEven)
                continue
            maxOdd = max(maxOdd, v)
        return maxOdd - minEven