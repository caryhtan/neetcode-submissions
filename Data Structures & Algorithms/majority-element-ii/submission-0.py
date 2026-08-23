class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        dic = {}
        arr = []
        for n in nums:
            dic[n] = dic.get(n, 0) + 1
        for n, cnt in dic.items():
            if cnt > (len(nums) // 3):
                arr.append(n)
        return arr