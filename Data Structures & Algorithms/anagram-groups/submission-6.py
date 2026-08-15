class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        for s in strs:
            newS = sorted(s)
            dic["".join(newS)].append(s)
        return list(dic.values())