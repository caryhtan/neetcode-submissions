class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = Counter(nums)
        arr = [[] for _ in range(len(nums) + 1)]
        for n, c in dic.items():
            arr[c].append(n)
        res = []
        for i in range(len(arr) - 1, -1, -1):
            for j in range(len(arr[i])):
                res.append(arr[i][j])
                if len(res) == k:
                    return res