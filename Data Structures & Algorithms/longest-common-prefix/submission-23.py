class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        first, last = strs[0], strs[-1]
        res = []
        for i in range(min(len(first), len(last))):
            if first[i] != last[i]:
                return "".join(res)
            res.append(first[i])
        return "".join(res)