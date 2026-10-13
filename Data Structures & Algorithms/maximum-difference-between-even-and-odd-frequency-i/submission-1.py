class Solution:
    def maxDifference(self, s: str) -> int:
        dic = Counter(s)
        oddNumF, evenNumF = 0, len(s)
        for f in dic.values():
            if (f % 2) != 0:
                oddNumF = max(f, oddNumF)
            else:
                evenNumF = min(f, evenNumF)
        return oddNumF - evenNumF