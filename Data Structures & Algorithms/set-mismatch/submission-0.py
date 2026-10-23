class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        mySet = set()
        for n in nums:
            if n in mySet:
                duplicate = n
            else:
                mySet.add(n)
        for n in range(1, len(nums) + 1):
            if n not in mySet:
                missing = n
        return [duplicate, missing]