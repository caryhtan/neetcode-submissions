class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        mySet = set()
        res = []
        for n in nums:
            if n in mySet:
                res.append(n)
                continue
            mySet.add(n)
        for i in range(1, len(nums) + 1):
            if i not in mySet:
                res.append(i)
        return res