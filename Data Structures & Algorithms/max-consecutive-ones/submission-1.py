class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cnt = 0
        maxCnt = 0
        for n in nums:
            if n == 1:
                cnt += 1
                maxCnt = max(maxCnt,cnt)
            else:
                cnt = 0
        return maxCnt