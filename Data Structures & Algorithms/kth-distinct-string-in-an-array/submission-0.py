class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        dic = Counter(arr)
        res = []
        for key, v in dic.items():
            if v == 1:
                res.append(key)
                continue
        index = k - 1
        if index < len(res):
            return res[index]
        else:
            return ""