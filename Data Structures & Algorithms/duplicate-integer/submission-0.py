class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for i in nums:
            # i already represent elements in nums
            if i not in seen:
                seen.add(i)
            else:
                return True
        return False