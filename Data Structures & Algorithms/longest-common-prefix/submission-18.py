class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        arr = []
        strs.sort()
        first, last = strs[0], strs[-1]
        i = 0
        while i < len(first):
            if first[i] != last[i]:
                return "".join(arr)
            arr.append(first[i])
            i += 1
        return "".join(arr)