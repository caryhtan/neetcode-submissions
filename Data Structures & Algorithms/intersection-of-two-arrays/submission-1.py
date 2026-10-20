class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        seen = set(nums1)
        arr = []
        for n in nums2:
            if n in seen:
                arr.append(n)
                seen.remove(n)
        return arr