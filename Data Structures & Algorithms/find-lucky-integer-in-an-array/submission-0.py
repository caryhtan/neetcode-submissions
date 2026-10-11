class Solution:
    def findLucky(self, arr: List[int]) -> int:
        cnt = Counter(arr)
        arr = []
        maxN = -1
        for n, c in cnt.items():
            if n == c:
                maxN = max(maxN, n)
        return maxN