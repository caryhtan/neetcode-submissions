class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        dic = defaultdict(int)
        for n in nums:
            dic[n] += 1
            if len(dic) <= 2:
                continue
            newDic = defaultdict(int)
            for key, val in dic.items():
                if val >= 2:
                    newDic[key] = val - 1
            dic = newDic
        res = []
        for n in dic:
            if nums.count(n) > (len(nums) // 3):
                res.append(n)
        return res