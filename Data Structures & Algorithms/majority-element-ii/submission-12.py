class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cnt = defaultdict(int)
        arr = []
        for n in nums:
            cnt[n] += 1
            if len(cnt) <= 2:
                continue
            newCnt = defaultdict(int)
            for key, value in cnt.items():
                if value > 1:
                    newCnt[key] = value - 1
            cnt = newCnt
        res = []
        for n in cnt:
            if nums.count(n) > (len(nums) // 3):
                res.append(n)
        return res