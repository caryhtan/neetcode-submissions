class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = curSum = 0
        dic = {0 : 1}
        for n in nums:
            curSum += n
            diff = curSum - k
            res += dic.get(diff, 0)
            dic[curSum] = dic.get(curSum, 0) + 1
        return res