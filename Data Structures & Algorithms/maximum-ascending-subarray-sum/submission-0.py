class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        res, currentSum = nums[0], nums[0]
        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                currentSum = 0
            currentSum += nums[i]
            res = max(currentSum, res)
        return res