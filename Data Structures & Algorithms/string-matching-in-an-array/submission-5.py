class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res = []
        for w in words:
            for w2 in words:
                if w != w2 and w in w2:
                    res.append(w)
                    break
        return res