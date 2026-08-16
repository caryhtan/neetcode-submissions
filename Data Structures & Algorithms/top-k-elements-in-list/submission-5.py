class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        arr = [[] for _ in range(len(nums) + 1)]
        for n in nums:
            dic[n] = dic.get(n, 0) + 1
        for key, v in dic.items():
            arr[v].append(key)
        res = []
        for i in range(len(arr) - 1, 0, -1):
            for j in range(len(arr[i])):
                res.append(arr[i][j])
                if len(res) == k:
                    return res