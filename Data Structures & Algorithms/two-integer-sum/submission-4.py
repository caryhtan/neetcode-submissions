class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff not in dic:
                dic[n] = i
            else:
                return [dic[diff], i]