class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        first, last, res = strs[0], strs[-1], []
        for i in range(min(len(first), len(last))):
            if first[i] != last[i]:
                return "".join(res)
            res.append(first[i])
        return "".join(res)