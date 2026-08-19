class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        arr = [[] for _ in range(len(nums) + 1)]
        for n in nums:
            dic[n] = dic.get(n, 0) + 1
        for n, c in dic.items():
            arr[c].append(n)
        res = []
        for i in range(len(arr) - 1, -1, -1):
            for j in range(len(arr[i])):
                res.append(arr[i][j])
                if len(res) == k:
                    return res