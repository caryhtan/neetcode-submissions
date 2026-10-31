class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res, cnt = 0, 0
        for n in nums:
            if n == 1:
                cnt += 1
            else:
                cnt = 0
            res = max(cnt, res)
        return res