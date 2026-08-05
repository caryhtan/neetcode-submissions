import random

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            n = random.choice(nums)
            cnt = nums.count(n)
            if cnt > (len(nums) // 2):
                return n