class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        mySet = set()
        for s in words:
            for s2 in words:
                if s == s2:
                    continue
                if s in s2:
                    mySet.add(s)
        return list(mySet)