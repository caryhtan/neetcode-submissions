class Solution:
    def swap(self, nums, x, y):
        nums[x], nums[y] = nums[y], nums[x]

    def sortColors(self, nums: List[int]) -> None:
        l, r, i = 0, len(nums) - 1, 0

        while i <= r:
            if nums[i] == 0:
                self.swap(nums, i, l)
                l += 1
            elif nums[i] == 2:
                self.swap(nums, i, r)
                r -= 1
                i -= 1
            i += 1