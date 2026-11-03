class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        res = []
        has = set()
        for n in nums:
            if n in has:
                res.append(n)
                continue
            has.add(n)
        for i in range(1, len(nums) + 1):
            if i not in has:
                res.append(i)
        return res