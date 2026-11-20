class Solution:

    def swap(self, nums, x : int, y : int) -> None:
        temp = nums[x]
        nums[x] = nums[y]
        nums[y] = temp
   
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, l, r = 0, 0, len(nums) - 1
        while i <= r:
            if nums[i] == 0:
                self.swap(nums, l, i)
                l += 1
            elif nums[i] == 2:
                self.swap(nums,r, i)
                i -= 1
                r -= 1
            i += 1