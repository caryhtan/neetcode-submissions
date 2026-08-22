class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        arr = []
        newS = sorted(strs)
        first = newS[0]
        last = newS[-1]
        for i in range(min(len(first), len(last))):
            if first[i] != last[i]:
                return "".join(arr)
            else:
                arr.append(first[i])
        return "".join(arr)