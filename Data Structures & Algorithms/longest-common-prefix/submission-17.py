class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        arr = []
        strs.sort()
        first, last = strs[0], strs[-1]
        for c in range(min(len(first), len(last))):
            if first[c] != last[c]:
                return "".join(arr)
            arr.append(first[c])
        return "".join(arr)