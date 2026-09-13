class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        cnt = 0
        arr = sorted(heights)
        for i in range(len(heights)):
            if heights[i] != arr[i]:
                cnt += 1
        return cnt