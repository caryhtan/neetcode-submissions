class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        arr = []
        new_strs = sorted(strs)
        first = new_strs[0]
        last = new_strs[-1]
        for c in range(min(len(first), len(last))):
            if first[c] != last[c]:
                return "".join(arr)
            arr.append(first[c])
        return "".join(arr)