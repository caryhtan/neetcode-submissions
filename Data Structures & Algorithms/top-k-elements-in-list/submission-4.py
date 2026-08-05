class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        buc = [[] for _ in range(len(nums)+1)]
        for n in nums:
            dic[n] = dic.get(n,0) + 1
        for n,c in dic.items():
            buc[c].append(n)
        res = []
        for i in range(len(buc)-1,0,-1):
            for j in range(len(buc[i])):
                res.append(buc[i][j])
                if len(res) == k:
                    return res