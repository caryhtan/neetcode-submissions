class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        dic = defaultdict(int)
        for w in words:
            for c in w:
                dic[c] += 1
        for c in dic:
            if dic[c] % len(words) != 0:
                return False
        return True