class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        for s in strs:
            new_s = sorted(s)
            dic["".join(new_s)].append(s)
        return list(dic.values())