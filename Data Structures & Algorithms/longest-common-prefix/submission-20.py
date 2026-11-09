class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        newStrs = sorted(strs)
        first, last = newStrs[0], newStrs[-1]
        res = []
        for i in range(min(len(first), len(last))):
            if first[i] != last[i]:
                return "".join(res)
            res.append(first[i])
        return "".join(res)