import random

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        while True:
            n = random.choice(nums)
            cnt = nums.count(n)
            if cnt > (len(nums) // 2):
                return n