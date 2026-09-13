class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        cnt = [0] * 101
        for h in heights:
            cnt[h] += 1
        arr = []
        for i in range(len(cnt)):
            for _ in range(cnt[i]):
                arr.append(i)
        index = 0
        for i in range(len(heights)):
            if heights[i] != arr[i]:
                index += 1
        return index