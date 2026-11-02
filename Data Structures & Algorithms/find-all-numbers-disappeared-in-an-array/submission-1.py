class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        mySet = set()
        arr = []
        for i in range(1, len(nums) + 1):
            mySet.add(i)
        for n in mySet:
            if n not in nums:
                arr.append(n)
        return arr