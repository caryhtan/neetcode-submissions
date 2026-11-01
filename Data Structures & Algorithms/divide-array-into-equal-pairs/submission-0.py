class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        if len(nums) % 2 != 0:
            return False
        seen = set()
        dic = Counter(nums)
        for c in dic.values():
            if c % 2 != 0:
                return False
        return True