class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        if len(arr) <= 1:
            return [-1]
        for i in range(len(arr)-1):
            tmpArr = arr[i+1:]
            maxVal = max(tmpArr)
            arr[i] = maxVal
        arr[i+1] = -1
        return arr