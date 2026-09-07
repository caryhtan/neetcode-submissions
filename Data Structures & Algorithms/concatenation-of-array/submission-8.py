class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        arr = [0] * 2 * len(nums)
        for i, n in enumerate(nums):
            arr[i] = n
            arr[len(nums) + i] = n
        return arr