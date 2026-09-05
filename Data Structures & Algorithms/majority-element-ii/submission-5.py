class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cnt = {}
        for n in nums:
            cnt[n] = cnt.get(n, 0) + 1
            if len(cnt) <= 2:
                continue
            new_cnt = {}
            for n, c in cnt.items():
                if c > 1:
                    new_cnt[n] = c - 1
            cnt = new_cnt
        res = []
        for n in cnt:
            if (nums.count(n) > len(nums) // 3):
                res.append(n)
        return res