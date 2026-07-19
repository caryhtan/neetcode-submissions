class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in dic:
                if i <= dic[diff]:
                    return [i, dic[diff]]
                else:
                    return [dic[diff], i]
            else:
                dic[n] = i