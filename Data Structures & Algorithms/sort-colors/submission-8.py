class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left, i = 0, 0
        right = len(nums) - 1
        def swap(x, y):
            temp = nums[x]
            nums[x] = nums[y]
            nums[y] = temp
        while i <= right:
            if nums[i] == 0:
                swap(i, left)
                left += 1
            elif nums[i] == 2:
                swap(i, right)
                right -= 1
                i -= 1
            i += 1
        return nums