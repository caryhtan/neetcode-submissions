class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(nums, L, M, R):
            left, right = nums[L:M+1], nums[M+1:R+1]
            i, l, r = L, 0, 0
            while l < len(left) and r < len(right):
                if left[l] <= right[r]:
                    nums[i] = left[l]
                    l += 1
                    i += 1
                    continue
                nums[i] = right[r]
                r += 1
                i += 1
            while l < len(left):
                nums[i] = left[l]
                l += 1
                i += 1
            while r < len(right):
                nums[i] = right[r]
                r += 1
                i += 1

        def mergeSort(nums, l, r):
            if l >= r:
                return
            m = (l + r) // 2
            mergeSort(nums, l, m)
            mergeSort(nums, m+1, r)
            merge(nums, l, m, r)

        mergeSort(nums, 0, len(nums) - 1)
        return nums