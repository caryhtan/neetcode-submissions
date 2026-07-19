class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        for s in strs:
            new_str = "".join(sorted(s))
            dic[new_str].append(s)
        return list(dic.values())