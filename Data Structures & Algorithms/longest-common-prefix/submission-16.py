class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        arr = []
        new_s = sorted(strs)
        first = new_s[0]
        last = new_s[-1]
        for i in range(min(len(first), len(last))):
            if first[i] != last[i]:
                return "".join(arr)
            arr.append(first[i])
        return "".join(arr)