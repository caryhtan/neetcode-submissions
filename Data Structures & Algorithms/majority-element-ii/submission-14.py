class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cnt = defaultdict(int)
        for n in nums:
            cnt[n] += 1
            if len(cnt) <= 2:
                continue
            newCnt = defaultdict(int)
            for key, val in cnt.items():
                if val >= 2:
                    newCnt[key] = val - 1
            cnt = newCnt
        res = []
        for n in cnt:
            if nums.count(n) > (len(nums) // 3):
                res.append(n)
        return res