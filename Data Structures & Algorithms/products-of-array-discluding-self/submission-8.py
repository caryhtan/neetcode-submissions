class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixP, postfixP = 1, 1
        res = [1] * len(nums)
        for i in range(len(nums)):
            res[i] = prefixP
            prefixP *= nums[i]
        for j in range(len(nums) - 1, -1, -1):
            res[j] *= postfixP
            postfixP *= nums[j]
        return res