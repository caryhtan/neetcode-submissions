class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        balloonDic = Counter("balloon")
        textDic = Counter(text)
        res = len(text)
        for c in balloonDic:
            res = min(res, textDic[c] // balloonDic[c])
        return res